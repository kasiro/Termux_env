use std::iter::Iterator;

pub struct Product {
    chars: Vec<char>,
    repeat: usize,
    indices: Vec<usize>,
}

impl Iterator for Product {
    type Item = String;

    fn next(&mut self) -> Option<Self::Item> {
        if self.indices.is_empty() {
            self.indices = vec![0; self.repeat];
        }

        let result: String = self.indices.iter().map(
            |&i| self.chars[i]
        ).collect();

        let mut carry = true;
        for i in (0..self.repeat).rev() {
            if carry {
                self.indices[i] += 1;
                if self.indices[i] >= self.chars.len() {
                    self.indices[i] = 0;
                } else {
                    carry = false;
                }
            }
        }

        if carry {
            return None;
        }

        Some(result)
    }
}

pub fn product_(s: String, repeat: usize) -> Product {
    let chars: Vec<char> = s.chars().collect();
    Product {
        chars,
        repeat,
        indices: vec![],
    }
}

macro_rules! product {
    ($arg1:expr, $arg2:expr) => {
        product_($arg1, $arg2);
    };
}
