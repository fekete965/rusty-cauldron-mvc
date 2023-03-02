-- migration-04

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Harry" as first_name,
    "Potter" as last_name,
    "harry-potter@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$BketHiHfFSjYyer0$6627a5cbb164963804e8ae772ee5d286a3f3d7b093390bc7f1fa636b59e4f336" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Hermione" as first_name,
    "Granger" as last_name,
    "hermione-granger@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$zryxQbVdEBtC6haz$b75abeddb0e4f26e2eb9ba9dd064d02ca1c9a76b3a16efe1551aae547712214f" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Tom" as first_name,
    "Riddle" as last_name,
    "tom-riddle@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$dfmEVOIbJJ9vWfp5$091b238103e7c85b3ab0382a9aa2e751211effc10a916cf9acd687a5220aeb47" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Albus" as first_name,
    "Dumbledore" as last_name,
    "albus-dumbledore@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$s1JrBdeimUvgOQBN$77c6405de16aaa93f108a1a64568f74f5980da3cec81d4588de2601d62e221a8" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Draco" as first_name,
    "Malfoy" as last_name,
    "draco-malfoy@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$w7YZMpiP8fP4VLAV$14b7d7255200df83e625991f1c56a6b4975bdb07c6b6fcec00d3126d1b1f6c9e" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);
  
INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Severus" as first_name,
    "Snape" as last_name,
    "severus-snape@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$tn7V2zY7q9bYxNMV$92e5b80c0a98898246dd2d1cdc847d4758b5c0b074927aa7ae31c222c4801875" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Rebeus" as first_name,
    "Hagrid" as last_name,
    "rebeus-hagrid@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$jkyIRmglhQruznYy$47080242623fa51113cd3b55bea0491b6487aeadedc1a984772e367ea844204c" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Ron" as first_name,
    "Weasley" as last_name,
    "ron-weasley@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$s30rYFTF7yLjDpw6$0331da5ac0ec5bfea8e1c2db700cbbb0dbbc60f706b56b7a1dfc9f41ac985fe9" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Luna" as first_name,
    "Lovegood" as last_name,
    "luna-lovegood@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$wLW4kzjWaeIcJUGZ$f867fa388a23c06de251a96b45fcda8db5319ccbb4f7e4fb92abc47bfb3e9be3" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Minerva" as first_name,
    "Mcgonagall" as last_name,
    "minerva-mcgonagall@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$rnLkZfAEYaGw71s4$9375f40ae8d97241a0fdfa56f12e180374fc37eb7fd3f5093eb1af941e1db824" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Dooby" as first_name, NULL as last_name, "dooby@owl-postal.co.uk" as email, "pbkdf2:sha256:260000$0hYLuR1dRzATLmOr$e147819676691371964c373eae76d6e08d3659cf2245470cd52c4e125834d9de" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Bellatrix" as first_name,
    "Lestrange" as last_name,
    "bellatrix-lestrange@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$UQqh3bkRmjXwhEx1$220548ee480b033a212845587fffdb3c92e3400b6fecf545a9761ff5a2ec031e" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Sirius" as first_name,
    "Black" as last_name,
    "sirius-black@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$m0EqduYnOhni4ETu$a3d1d420484f2c4b9cb337e80d8f9ebc711412987dcd48910379309185a7b8c2" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Neville" as first_name,
    "Longbottom" as last_name,
    "neville-longbottom@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$paCFtFf5oULVsE6A$ef880246421aee549e806a83a645e9048af1d741e794402d2942648c0984c5b8" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Remus" as first_name,
    "Lupin" as last_name,
    "remus-lupin@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$yJXiTUlFL81nsixP$12b996f5d05b02f20e64a810e513503d46e77ec250ac6ca03c06c29dec5b3740" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Dolores" as first_name,
    "Umbridge" as last_name,
    "dolores-umbridge@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$hupy1M5HrUw32zk0$d986432cb9d5fc8343e6f6c50643521815ccdfb021569fb37ce22b1c4e7e5fd2" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Gellert" as first_name,
    "Grindewald" as last_name,
    "gellert-grindewald@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$RiOTYJjwO9d0XXlJ$e6a1721efa13135729d87ff813fa1f52e19c1313b56cf747fcbab91d4fd54ace" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Ginny" as first_name,
    "Weasley" as last_name,
    "ginny-weasley@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$PCQY4ym2yqKit1SB$cb77dc79d1ff9b2c3e9ecc42353337f670cee8d293bde8ae3a0b8a3217ab731e" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Peter" as first_name,
    "Pettigrew" as last_name,
    "peter-pettigrew@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$HyFgLlfqtDkqedM3$a266729869c273814b58603d2f29f281528506333982ecea464017dfc60afea4" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Newt" as first_name,
    "Scamander" as last_name,
    "newt-scamander@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$PshPAhl1CZuo1R1x$57255e379ef7c6eee542a82f0fea6c41fd2de617d70a639eb9fc753e8081b0a5" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Lily" as first_name,
    "Potter" as last_name,
    "lily-potter@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$H6aQzyEigfa7ho3M$bb37ffcfd9529354c17ecca14355abace58f2eca45c57899bd4bf9f7f8c14bc6" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Lucius" as first_name,
    "Malfoy" as last_name,
    "lucius-malfoy@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$2AT2Wc2bMPVcct7Z$d21d1946edcdd45a1b6a97f5e38a0ae39fed3582784e9d7ded4acd28245fbcd3" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Dudley" as first_name,
    "Dursley" as last_name,
    "dudley-dursley@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$etfkiWYJH0eK3zFq$800541364d22e7bb58c7d7fdea5828aa58efcc1acdb811aef8001c94dd6fc409" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Nymphadora" as first_name,
    "Tonks" as last_name,
    "nymphadora-tonks@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$3kUhMiLhlfSQrj2J$eb61c281ff186bf976fb030e4c50cb96f92b6d85b0e9b4aa2c9b596bbb5f677d" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Alastor" as first_name,
    "Moody" as last_name,
    "alastor-moody@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$fvt9NmlvvIeEZl7v$c369259d12c3d41dd0a585644cf15b551bc24f68758a4c8eb003db3e23e005ec" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Fleur" as first_name,
    "Delacour" as last_name,
    "fleur-delacour@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$3vrhTAJUjogsWocq$2e81501fb76d51125d52aceb10e5a7c0d99e835ad8c2f09f5d070b9ebfd71bf1" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "Argus" as first_name,
    "Filch" as last_name,
    "argus-filch@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$RlrYAfgkCGUA2xxd$dceb4dc86c9f330bf38184857eafa79b47703838492d4f88dbe28b1a0e057952" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);

INSERT INTO users (first_name, last_name, email, password)
SELECT first_name, last_name, email, password 
FROM (
  SELECT
    "James" as first_name,
    "Potter" as last_name,
    "james-potter@owl-postal.co.uk" as email,
    "pbkdf2:sha256:260000$3g04uFp1AREu3hlr$e9ddfc1fabde402bf627368bb058a9dac7e1387ccf9111ba37a3db63c786c436" as password
  ) u
WHERE NOT EXISTS (SELECT 1 FROM users WHERE users.email = u.email);
