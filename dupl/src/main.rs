use std::collections::HashMap;
use serde_json;
use serde::Serialize;
use serde;

//trait UpLow {
//    fn upper(self) -> char;
//    fn lower(self) -> char;
//}
//
//impl UpLow for char {
//    
//    fn upper(self) -> char {
//        self.to_uppercase().next().expect("REASON")
//    }
//
//    fn lower(self) -> char {
//        self.to_lowercase().next().expect("REASON")
//    }
//
//}

pub struct MyHashMap<K, V> {
    inner: HashMap<K, V>
}

impl<K, V> MyHashMap<K, V>
 where K: std::cmp::Eq + std::hash::Hash {
    pub fn new(map: HashMap<K, V>) -> Self {
        Self { inner: map }
    }

    pub fn get(&self, key: K) -> V
     where V: Clone {
        self.inner.get(&key).unwrap().clone()
    }
}

impl<V, K> std::ops::Deref for MyHashMap<K, V>
 where K: std::cmp::Eq + std::hash::Hash {
    type Target = HashMap<K, V>;

    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

macro_rules! hashmap {
    ($( $key:expr => $value:expr ),*) => {{
        let mut map = HashMap::new();
        $(
            map.insert($key, $value);
        )*
        map
    }};
}

//fn get_dup(s: &str) -> (usize, Vec<char>) {
//    let mut cc: HashMap<char, usize> = HashMap::new();
//    let mut uchars: Vec<char> = Vec::new();
//
//    for c in s.chars() {
//        *cc.entry(c).or_insert(0) += 1;
//        if cc[&c] == 1 {
//            uchars.push(c);
//        }
//    }
//
//    let rc: usize = cc.values().filter(
//        |&&count| count > 1
//    ).count();
//
//    (rc, uchars)
//}

trait PrettyPrint {
    fn pp(&self) -> String;
}

impl<K, V> PrettyPrint for HashMap<K, V>
where
    K: std::hash::Hash + Eq + serde::Serialize,
    V: serde::ser::Serialize,
{
    fn pp(&self) -> String {
        serde_json::to_string_pretty(
            &self
        ).unwrap()
    }

}

fn main() {
//    let s = "446890912aAfFtt";
//    let result = get_dup(s);
//    println!("{:?}", result);
    let d = hashmap! {
        "classes" => hashmap! {
            "Cargo" => hashmap! {
                "new" => "Cargo<self>::new()",
                "pp" => "Cargo::pp()"
            }
        }
    };
    println!(
        "{}",
        d.pp()
    );
}
