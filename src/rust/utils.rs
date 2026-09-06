/// Normalize a possibly-negative Python-style index against a collection length.
pub fn normalize_index(index: isize, len: usize) -> Option<usize> {
    let len = len as isize;
    let idx = if index < 0 { index + len } else { index };
    (idx >= 0 && idx < len).then_some(idx as usize)
}
