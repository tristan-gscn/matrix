import math
import pytest
from matrix import Matrix
from matrix.ex14.projection import projection


class TestProjectionMatrix:
    def test_standard_frustum_column_major(self) -> None:
        # fov = 90 deg => tan(45 deg) = 1.0
        # ratio = 1.0 => sx = 1.0, sy = 1.0
        # near = 1.0, far = 10.0 => c = -10/9, d = -10/9
        p = projection(90.0, 1.0, 1.0, 10.0, column_major=True)
        c = -10.0 / 9.0
        d = -10.0 / 9.0
        expected = Matrix([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, c, -1.0],
            [0.0, 0.0, d, 0.0],
        ])
        assert p == expected

    def test_standard_frustum_row_major(self) -> None:
        p = projection(90.0, 1.0, 1.0, 10.0, column_major=False)
        c = -10.0 / 9.0
        d = -10.0 / 9.0
        expected = Matrix([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, c, d],
            [0.0, 0.0, -1.0, 0.0],
        ])
        assert p == expected

    def test_column_major_is_transpose_of_row_major(self) -> None:
        p_col = projection(60.0, 16.0 / 9.0, 0.5, 100.0, column_major=True)
        p_row = projection(60.0, 16.0 / 9.0, 0.5, 100.0, column_major=False)
        assert p_col == p_row.transpose()

    def test_radians_mode(self) -> None:
        p_deg = projection(90.0, 1.5, 0.1, 50.0, radians=False)
        p_rad = projection(math.pi / 2.0, 1.5, 0.1, 50.0, radians=True)
        assert p_deg == p_rad

    def test_ratio_affects_only_x_scale(self) -> None:
        p1 = projection(90.0, 1.0, 1.0, 10.0, column_major=False)
        p2 = projection(90.0, 2.0, 1.0, 10.0, column_major=False)
        # sx for p2 should be half of p1
        c = -10.0 / 9.0
        d = -10.0 / 9.0
        expected1 = Matrix([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, c, d],
            [0.0, 0.0, -1.0, 0.0],
        ])
        expected2 = Matrix([
            [0.5, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, c, d],
            [0.0, 0.0, -1.0, 0.0],
        ])
        assert p1 == expected1
        assert p2 == expected2

    def test_ndc_depth_mapping_formula(self) -> None:
        near = 0.5
        far = 100.0
        c = -far / (far - near)
        d = -(far * near) / (far - near)

        # At z = -near: z_ndc = (c * -near + d) / near == 0.0
        z_near_ndc = (c * (-near) + d) / near
        assert abs(z_near_ndc) < 1e-9

        # At z = -far: z_ndc = (c * -far + d) / far == 1.0
        z_far_ndc = (c * (-far) + d) / far
        assert abs(z_far_ndc - 1.0) < 1e-9

    def test_invalid_near_plane(self) -> None:
        with pytest.raises(ValueError, match="near plane must be positive"):
            projection(90.0, 1.0, 0.0, 10.0)
        with pytest.raises(ValueError, match="near plane must be positive"):
            projection(90.0, 1.0, -1.0, 10.0)

    def test_invalid_far_plane(self) -> None:
        with pytest.raises(ValueError, match="strictly greater"):
            projection(90.0, 1.0, 5.0, 5.0)
        with pytest.raises(ValueError, match="strictly greater"):
            projection(90.0, 1.0, 5.0, 2.0)

    def test_invalid_ratio(self) -> None:
        with pytest.raises(ValueError, match="aspect ratio must be positive"):
            projection(90.0, 0.0, 1.0, 10.0)
        with pytest.raises(ValueError, match="aspect ratio must be positive"):
            projection(90.0, -1.5, 1.0, 10.0)

    def test_invalid_fov(self) -> None:
        with pytest.raises(ValueError, match="fov must be in range"):
            projection(0.0, 1.0, 1.0, 10.0)
        with pytest.raises(ValueError, match="fov must be in range"):
            projection(180.0, 1.0, 1.0, 10.0)
        with pytest.raises(ValueError, match="fov must be in range"):
            projection(-45.0, 1.0, 1.0, 10.0)


class TestMatrixDisplayIntegration:
    def test_display_environment(self) -> None:
        import os
        from pathlib import Path

        display_dir = Path(__file__).resolve().parent / "display"
        assert display_dir.is_dir()
        assert (display_dir / "assets" / "logo.png").is_file()
        assert (display_dir / "assets" / "model.obj").is_file()
        launcher = display_dir / "display"
        assert launcher.is_file()
        assert os.access(launcher, os.X_OK)

    def test_proj_format_compliance(self) -> None:
        from pathlib import Path

        display_dir = Path(__file__).resolve().parent / "display"
        proj_file = display_dir / "proj"
        assert proj_file.is_file()

        lines = [
            line.strip()
            for line in proj_file.read_text().splitlines()
            if line.strip()
        ]
        assert len(lines) == 4
        for line in lines:
            parts = [p.strip() for p in line.split(",")]
            assert len(parts) == 4
            for val in parts:
                f = float(val)
                assert math.isfinite(f)

    def test_display_execution_smoke(self) -> None:
        import subprocess
        from pathlib import Path

        display_dir = Path(__file__).resolve().parent / "display"
        launcher = display_dir / "display"
        if not (launcher.is_file() and (display_dir / "proj").is_file()):
            pytest.skip("display environment not fully populated")

        proc = subprocess.Popen(
            ["./display"],
            cwd=str(display_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            proc.wait(timeout=0.4)
            assert proc.returncode == 0
        except subprocess.TimeoutExpired:
            proc.terminate()
            proc.wait()
