CREATE TABLE IF NOT EXISTS water_monitor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    start_time VARCHAR(32),
    end_time VARCHAR(32),
    duration INT,
    release_date TIMESTAMP,
    create_date TIMESTAMP,
    update_date TIMESTAMP
) ENGINE=INNODB;