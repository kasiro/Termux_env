pub use std::time::{Instant, Duration};

pub fn rtd(value: f64, decimals: usize) -> f64 {
    if decimals == 0 {
        value.trunc()
    } else {
        (value * 10_f64.powi(
            decimals as i32
        )).round() / 10_f64.powi(decimals as i32)
    }
}

pub fn fv(value: f64, decimals: usize) -> String {
    format!(
        "{:.*}",
        decimals,
        rtd(value, decimals)
    )
}

pub fn round(s: Duration, mut decimals: usize) -> String {
    let total_seconds = s.as_secs_f64();
    let minutes = total_seconds / 60.0;
    let seconds = total_seconds % 60.0;

    if minutes >= 1.0 {
        decimals = 0;
        format!(
            "{}m {}s", 
            fv(minutes, decimals),
            fv(seconds, decimals)
        )
    } else {
        format!("{}s", fv(seconds, decimals))
    }
}

#[macro_export]
macro_rules! get_time {
    ($code:block) => {
        let start = Instant::now();
        $code
        let end = Instant::now();
        println!(
            "Time elapsed: {:?}",
            self::round(
                end.duration_since(start), 2
            )
        );
    }
}
