struct Seclude<'a> {
    api_key: &'a str
}

impl Seclude<'_> {
    
    fn key(&self) -> &str {
        self.api_key
    }

}

fn main() {
    let sec = Seclude {
        api_key: "h-r:7"
    };
    println!("{}", sec.key());
}
