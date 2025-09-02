use std::error::Error;
use std::fs::File;

use chrono::prelude::*;
use polars::prelude::*;

fn main() -> Result<(), Box<dyn Error>> {
    let mut df: DataFrame = df!(
        "integer" => &[1, 2, 3],
        "date" => &[
                NaiveDate::from_ymd_opt(2025, 1, 1).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                NaiveDate::from_ymd_opt(2025, 1, 2).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                NaiveDate::from_ymd_opt(2025, 1, 3).unwrap().and_hms_opt(0, 0, 0).unwrap(),
        ],
        "float" => &[4.0, 5.0, 6.0],
        "string" => &["a", "b", "c"],
    )
        .unwrap();
    println!("{}", df);

    let mut file = File::create("output.csv").expect("could not create file");
    CsvWriter::new(&mut file)
        .include_header(true)
        .with_separator(b',')
        .finish(&mut df)?;
    let df_csv = CsvReader::from_path("output.csv").unwrap()
        .infer_schema(None)
        .has_header(true)
        .finish()?;
    println!("{}", df_csv);

    let out = df.clone().lazy().select([col("*")]).collect()?;
    println!("{}", out);

    return Ok(());
}
