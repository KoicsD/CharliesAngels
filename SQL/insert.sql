USE BloodDonations;

INSERT INTO donors
(
    name,
    weight,
    gender,
    date_of_birth,
    last_donation,
    last_month_sickness,
    unique_identifier,
    expiration_of_id,
    blood_type,
    hemoglobin,
    email,
    mobil
)
VALUES
(
    "Kiss Bela",
    "85",
    "male",
    "1990-05-30",
    "2015-01-01",
    "no",
    "654987AS",
    "2017-10-10",
    "B-",
    "112",
    "kiss@bela.com",
    "+36306543251"
);

INSERT INTO donors
(
    name,
    weight,
    gender,
    date_of_birth,
    last_donation,
    last_month_sickness,
    unique_identifier,
    expiration_of_id,
    blood_type,
    hemoglobin,
    email,
    mobil
)
VALUES
(
    "Nagy Olga",
    "65",
    "female",
    "1995-10-06",
    "2015-10-01",
    "no",
    "987623CV",
    "2019-01-10",
    "A-",
    "150",
    "nagyolga@kisvagy.hu",
    "+36306543251"
);

INSERT INTO donors
(
    name,
    weight,
    gender,
    date_of_birth,
    last_donation,
    last_month_sickness,
    unique_identifier,
    expiration_of_id,
    blood_type,
    hemoglobin,
    email,
    mobil
)
VALUES
(
    "Samsung Lajcsi",
    "95",
    "male",
    "1990-01-01",
    "2014-10-01",
    "yes",
    "123456AB",
    "2016-10-10",
    "0-",
    "160",
    "asdasd@qwerty.com",
    "+36205896321"
);

INSERT INTO donors
(
    name,
    weight,
    gender,
    date_of_birth,
    last_donation,
    last_month_sickness,
    unique_identifier,
    expiration_of_id,
    blood_type,
    hemoglobin,
    email,
    mobil
)
VALUES
(
    "Kiszel Donatella",
    "100",
    "female",
    "1970-08-06",
    "2015-0,-01",
    "no",
    "987654RT",
    "2018-01-23",
    "B-",
    "98",
    "kiszel@donatellacska.ru",
    "+36304152369"
);

INSERT INTO donations
(
    id,
    date_of_event,
    start_time,
    end_time,
    zip_code,
    city,
    address,
    number_of_available_beds,
    planned_donor_number,
    final_donor_number
)
VALUES
(
    "1",
    "2015-11-02",
    "8:00",
    "14:00",
    "3525",
    "Miskolc",
    "Regi posta utca 9.",
    "3",
    "45",
    "48"
);

INSERT INTO donations
(
    id,
    date_of_event,
    start_time,
    end_time,
    zip_code,
    city,
    address,
    number_of_available_beds,
    planned_donor_number,
    final_donor_number
)
VALUES
(
    "2",
    "2016-01-01",
    "10:00",
    "16:00",
    "3516",
    "Miskolc",
    "Futo utca 35.",
    "4",
    "55",
    "65"
);

INSERT INTO donations
(
    id,
    date_of_event,
    start_time,
    end_time,
    zip_code,
    city,
    address,
    number_of_available_beds,
    planned_donor_number,
    final_donor_number
)
VALUES
(
    "3",
    "2015-12-15",
    "9:00",
    "14:00",
    "3950",
    "Sarospatak",
    "Arany Janos ut 12.",
    "3",
    "35",
    "45"
);

INSERT INTO donations
(
    id,
    date_of_event,
    start_time,
    end_time,
    zip_code,
    city,
    address,
    number_of_available_beds,
    planned_donor_number,
    final_donor_number
)
VALUES
(
    "4",
    "2016-02-23",
    "10:00",
    "16:00",
    "3536",
    "Miskolc",
    "Patak u. 5.",
    "5",
    "40",
    "34"
);
