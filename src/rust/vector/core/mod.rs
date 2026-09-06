//! Base functionality for `Vector`: construction, indexing, iteration,
//! equality and display. Each exercise gets its own sibling module
//! (e.g. `vector::ex00`) once it's implemented.

mod copy;
mod eq;
mod getitem;
mod into_iter;
mod iterator;
mod len;
mod new;
mod repr;

pub use iterator::VectorIter;
