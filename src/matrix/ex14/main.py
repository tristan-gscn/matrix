import math
from matrix.ex14.projection import projection


def demo_projection_matrix() -> None:
    print("--- [ex14] 3D Perspective Projection Matrix ---")
    fov = 90.0
    ratio = 16.0 / 9.0
    near = 1.0
    far = 100.0

    p_col = projection(fov, ratio, near, far, column_major=True)
    p_row = projection(fov, ratio, near, far, column_major=False)

    print(
        f"Parameters: FOV={fov}°, ratio={ratio:.4f} (16:9), "
        f"near={near}, far={far}\n"
    )
    print("Projection matrix (Column-major for 42 display software):")
    print(p_col)
    print("\nProjection matrix (Row-major):")
    print(p_row)


def demo_ndc_verification() -> None:
    print("\n--- [ex14] Verification of NDC mapping ---")
    fov = 90.0
    ratio = 1.0
    near = 1.0
    far = 10.0

    tan_half = math.tan(math.radians(fov) / 2.0)
    top = near * tan_half
    right = top * ratio

    c = -far / (far - near)
    d = -(far * near) / (far - near)

    points = [
        ("Near center (0, 0, -near)", 0.0, 0.0, -near),
        ("Far center (0, 0, -far)", 0.0, 0.0, -far),
        ("Frustum corner (right, top, -near)", right, top, -near),
    ]

    for label, x, y, z in points:
        xc = x / (ratio * tan_half)
        yc = y / tan_half
        zc = c * z + d
        wc = -z

        x_ndc = xc / wc
        y_ndc = yc / wc
        z_ndc = zc / wc

        print(
            f"{label:35} -> NDC: ({x_ndc:5.2f}, {y_ndc:5.2f}, {z_ndc:5.2f})"
        )


def main() -> None:
    print("========================================")
    print("   Exercise 14: Bonus Projection Matrix  ")
    print("========================================")
    demo_projection_matrix()
    demo_ndc_verification()


if __name__ == "__main__":
    main()
