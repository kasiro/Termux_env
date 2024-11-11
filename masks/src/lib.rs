use std::str::Chars;

pub struct MaskProcessor<'a> {
    mask: Chars<'a>,
    current: Option<String>,
    stack: Vec<(String, Chars<'a>)>,
}

impl<'a> MaskProcessor<'a> {
    fn new(mask: &'a str) -> Self {
        MaskProcessor {
            mask: mask.chars(),
            current: Some(String::new()),
            stack: vec![],
        }
    }
}

impl<'a> Iterator for MaskProcessor<'a> {
    type Item = String;

    fn next(&mut self) -> Option<Self::Item> {
        while let Some((current, mut mask)) = self.stack.pop() {
            if let Some(ch) = mask.next() {
                if ch == '?' {
                    if let Some(next_char) = mask.next() {
                        match next_char {
                            'l' => {
                                for c in ('a'..='z').rev() {
                                    let mut new_password = current.clone();
                                    new_password.push(c);
                                    self.stack.push((new_password, mask.clone()));
                                }
                            }
                            'u' => {
                                for c in ('A'..='Z').rev() {
                                    let mut new_password = current.clone();
                                    new_password.push(c);
                                    self.stack.push((new_password, mask.clone()));
                                }
                            }
                            's' => {
                                let sp_ = r#"!\#$%&\'(\)*+,-\.\/:;<=>?@[\]^_`{|}~"#;
                                    for c in sp_.chars() {
                                        let mut new_password = current.clone();
                                        new_password.push(c);
                                        self.stack.push((new_password, mask.clone()));
                                    }
                            }
                            'd' => {
                                for c in ('0'..='9').rev() {
                                    let mut new_password = current.clone();
                                    new_password.push(c);
                                    self.stack.push((new_password, mask.clone()));
                                }
                            }
                            _ => {
                                let mut new_password = current.clone();
                                new_password.push('?');
                                new_password.push(next_char);
                                self.stack.push((new_password, mask));
                            }
                        }
                    } else {
                        let mut new_password = current.clone();
                        new_password.push('?');
                        self.stack.push((new_password, mask));
                    }
                } else {
                    let mut new_password = current.clone();
                    new_password.push(ch);
                    self.stack.push((new_password, mask));
                }
            } else {
                return Some(current);
            }
        }

        if let Some(current) = self.current.take() {
            self.stack.push((current, self.mask.clone()));
            return self.next();
        }

        None
    }
}

pub fn mask(mask: &str) -> MaskProcessor {
    MaskProcessor::new(mask)
}
