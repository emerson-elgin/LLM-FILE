use std::fs;

pub fn list_files(directory: &str) -> Vec<String> {
    match fs::read_dir(directory) {
        Ok(entries) => entries
            .filter_map(|entry| entry.ok().and_then(|e| e.path().to_str().map(String::from)))
            .collect(),
        Err(_) => vec![],
    }
}

pub fn file_metadata(file_path: &str) -> Option<fs::Metadata> {
    fs::metadata(file_path).ok()
}
