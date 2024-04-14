create table gym_user(
    user_id             SERIAL,
    user_type           VARCHAR(255),
    username            VARCHAR(255) unique not null,
    user_password       VARCHAR(255) NOT NULL,

    primary key (user_id)
);

create table gym_member(
    member_id           SERIAL,
    user_id             INT,
    first_name          VARCHAR(50) not null, 
    last_name           VARCHAR(50) not null,
    phone               VARCHAR(20) not null,
    email               VARCHAR(50) not null, 
    payment_info        TEXT,        
    subscription_type   VARCHAR(50) not null,
    subscription_start  DATE, 
    subscription_end    DATE, 
    member_weight       DECIMAL(5,2),
    member_height       DECIMAL(5,2),
    weight_goals        DECIMAL(5,2),
    num_workouts_week   INT,
    calorie_burn_goal   INT,
    saved_routines      TEXT,        

    primary key (member_id),
    foreign key (user_id) references gym_user
);

create table bill(
    paid                BOOLEAN,
    member_id           INT,

    foreign key (member_id) references gym_member
);

create table gym_admin(
    admin_id            SERIAL,
    user_id             INT,
    admin_first_name    VARCHAR(50) not null,
    admin_last_name     VARCHAR(50) not null,
    email               VARCHAR(50) unique not null,
    phone               VARCHAR(20) unique not null,
    admin_role          VARCHAR(20) not null,

    primary key (admin_id),
    foreign key (user_id) references gym_user
);

create table gym_trainer(
    trainer_id          SERIAL,
    user_id             INT,
    first_name          VARCHAR(50) not null,
    last_name           VARCHAR(50) not null,
    phone               VARCHAR(20) unique not null,
    email               VARCHAR(50) unique not null,
    specialization      VARCHAR(50) not null, --cardio, weights, etc.
    
    primary key (trainer_id),
    foreign key (user_id) references gym_user
);

create table gym_schedule(
    schedule_id         SERIAL,
    available_time      TIME,
    booking_length      VARCHAR(20), 
    trainer_id          INT,
    day_of_week         VARCHAR(20),

    primary key (schedule_id),
    foreign key (trainer_id) references gym_trainer
);

create table gym_room(
    room_id             SERIAL,
    room_name           VARCHAR(255) not null,
    room_number         INT,
    room_capacity       INT,
    room_availability   BOOLEAN,

    primary key (room_id)
);

create table gym_class(
    class_id            SERIAL,
    room_id             INT,
    trainer_id          INT,
    class_type          VARCHAR(20) not null, --individual, group
    category            VARCHAR(20) not null, --cardio, weights, etc               
    start_time          TIMESTAMP WITHOUT TIME ZONE,
    end_time            TIMESTAMP WITHOUT TIME ZONE,
    number_of_people    INT,
    enrollment_limit    INT,

    primary key (class_id),
    foreign key (room_id) references gym_room,
    foreign key (trainer_id) references gym_trainer
);

create table gym_equipment(
    equipment_id        SERIAL,
    equipment_name      VARCHAR(100),
    last_maintained     DATE,
    room_id             INT,

    primary key(equipment_id),
    foreign key(room_id) references gym_room
);

CREATE TABLE booked_classes (
    member_id           INT,
    class_id            INT,
    
    foreign key (member_id) references gym_member(member_id),
    foreign key (class_id) references gym_class(class_id),
    primary key (member_id, class_id)
);