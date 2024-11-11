#![allow(warnings)]
#[macro_use]
mod product;
mod gts;
use gts::*;
use product::*;
use fastrand;
use md5;
use num_format::{Locale, ToFormattedString};
use std::thread::sleep;
use std::time::Duration;

fn grc(string: &str, n: i32) -> String {
    let chars: Vec<char> = string.chars().collect();
    let mut result = String::new();
    for _ in 0..n {
        result.push(
            chars[
                fastrand::usize(0..chars.len())
            ]
        );
    }
    result
}

fn md5_(input: &str) -> String {
    let result = md5::compute(input.as_bytes());
    format!("{:x}", result)
}

fn put_chars(s: &mut String, ch: &str) {
    let v: Vec<char> = ch.chars().collect();
    for c in v {
        s.push(c);
    }
}

fn add_chars(s: &mut String, start: char, end: char) {
    for c in start..=end {
        s.push(c);
    }
}

fn ff(num: usize) -> String {
    num.to_formatted_string(
        &Locale::en
    ).replace(",", "_")

}

fn main() {
    let mut my_alf = String::new();
    // add_chars(&mut my_alf, 'A', 'Z');
    add_chars(&mut my_alf, 'a', 'z');
    add_chars(&mut my_alf, '0', '9');
    put_chars(&mut my_alf, "_-!?.:@%$#&+ ");
    // let hash = md5_("ab_rt");
    let hash = "7c85694d362017a3a861d36efd9e462e";
    get_time!({
        let mut c = true;
        let mut count_ = 0;
        for i in 1..6 {
            for pass in product!(my_alf.clone(), i) {
                if c == true {
                    count_ += 1;
                    // print!(
                    //     "\rskiped [{}]",
                    //     ff(count_)
                    // );
                    match pass.as_str() {
                        "c2k#!" => {
                            c = false;
                        },
                        _ => continue
                    }
                }
                if md5_(&pass) == hash {
                    println!("password: {}", pass);
                    break;
                }
                println!("{}", pass);
            }
        }
    });
}
