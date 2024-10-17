CREATE USER 's_akses'@'localhost' IDENTIFIED BY '12345';

CREATE USER 'l_akses'@'localhost' IDENTIFIED BY '45678';

GRANT SELECT, INSERT, UPDATE, DELETE ON tubes.Buku TO 'l_akses'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON tubes.Rata_Nilai_si TO 'l_akses'@'localhost';

GRANT ALL PRIVILEGES ON tubes.* TO 's_akses'@'localhost';

GRANT INSERT, UPDATE, DELETE, SELECT ON tubes.* TO 's_akses'@'localhost';

-- Apply the changes made with GRANT statements
FLUSHPRIVILEGES;