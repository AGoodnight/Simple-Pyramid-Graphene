DROP DATABASE hack_wizard;
CREATE DATABASE hack_wizard;

\c hack_wizard;

/* Create Wizard Session Table */
CREATE TABLE wsessions (
    id SERIAL PRIMARY KEY,
    completedSteps VARCHAR(255)[] DEFAULT ARRAY[]::VARCHAR(255)[],
    currentStep VARCHAR(255)
);

CREATE SEQUENCE wsessions_sequence
    start 1
    increment 1;

INSERT INTO wsessions 
    (id,completedSteps, currentStep) 
    VALUES 
    (
        nextval('wsessions_sequence'),
        ARRAY[]::VARCHAR(255)[],
        'address'
    );

/* Create Answers Table */
CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    wsession SERIAL NOT NULL REFERENCES wsessions(id),
    stepKey VARCHAR(50) NOT NULL,
    answer VARCHAR(255)
);

CREATE SEQUENCE answers_sequence
    start 1
    increment 1;

INSERT INTO answers 
    (id, wsession, stepKey, answer) 
    VALUES 
    (
        nextval('answers_sequence'),
        currval('wsessions_sequence'),
        'address',
        '1234 Washington Boulevard'
    );

/* Create Wizard Step Table */
CREATE TABLE steps (
    id SERIAL PRIMARY KEY,
    index INTEGER NOT NULL,
    complete BOOLEAN DEFAULT FALSE,
    schemaKey VARCHAR(50) NOT NULL
);

CREATE SEQUENCE steps_sequence
    start 1
    increment 1;

INSERT INTO steps 
    (id,index, complete,schemaKey) 
    VALUES 
    (
        nextval('steps_sequence'),
        '1',
        FALSE,
        'address'
    );




