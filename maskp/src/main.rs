use md5;
use masks::mask;
use std::fs::File;
use std::io::{BufReader, BufRead, Result};
use std::path::Path;
use std::env;
// use std::thread::sleep;
// use std::time::Duration;
// use std::process::exit;

fn md5_(t: &str) -> String {
    format!("{:x}", md5::compute(t))
}

fn ff<F>(name: &str, callback: F) -> Result<()>
where F: Fn(String) -> bool {
    let file = File::open(path_(name)?).expect("Unable to open file!");
    let reader = BufReader::new(file);

    for line in reader.lines() {
        match line {
            Ok(line) => {
                if callback(line) == true {
                    break;
                }
            },
            Err(e) => println!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn path_(relative_path: &str) -> Result<String> {
    // Получаем текущую директорию
    let mut current_dir = env::current_dir()?;
    let mut f = file!();
    f = &f[..(f.len() - 8)];
    current_dir.push(f);
    
    // Разделяем путь на компоненты
    let components = Path::new(relative_path).components();
    
    for component in components {
        match component {
            std::path::Component::CurDir => {
                // Игнорируем текущую директорию (.)
            },
            std::path::Component::ParentDir => {
                // Переходим на директорию выше (..)
                current_dir.pop();
            },
            std::path::Component::Normal(part) => {
                // Переходим в поддиректорию
                current_dir.push(part);
            },
            _ => {}
        }
    }
    
    // Преобразуем PathBuf в строку и возвращаем
    current_dir.to_str()
        .map(|s| s.to_string())
        .ok_or_else(|| std::io::Error::new(std::io::ErrorKind::Other, "Failed to convert path to string"))
}

fn main() -> Result<()> {
    let h = "7c85694d362017a3a861d36efd9e462e";
    // let _ = ff("../../downloads/3WiFi_WiFiKey.txt", |s| {
    //     if md5_(&s) == h {
    //         println!("password: {}", s);
    //         return true;
    //     }
    //     println!("{}", s);
    //     return false;
    // });
    for s in mask("") {
        if md5_(&s) == h {
            println!("password: {}", s);
            break;
        }
        println!("{}", s);
    }
    Ok(())
} 
