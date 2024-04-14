-- Add gym users
INSERT INTO gym_user (user_type, username, user_password) VALUES
('member', 'john_doe', 'password123'),
('member', 'jane_smith', 'pass123'),
('admin', 'admin_user', 'admin_pass'),
('trainer', 'trainer1', 'trainer_pass');

-- Add gym members
INSERT INTO gym_member (user_id, first_name, last_name, phone, email, payment_info, subscription_type, subscription_start, subscription_end, member_weight, member_height, weight_goals, num_workouts_week, calorie_burn_goal, saved_routines) VALUES
(1, 'John', 'Doe', '1234567890', 'john.doe@example.com', 'Credit Card', 'premium', '2023-01-01', '2024-01-01', 180.5, 70.5, 160.0, 3, 500, 'Routine 1, Routine 2'),
(2, 'Jane', 'Smith', '9876543210', 'jane.smith@example.com', 'PayPal', 'basic', '2023-02-01', '2024-02-01', 150.0, 65.0, 140.0, 2, 400, 'Routine 3, Routine 4');

-- Add bills
INSERT INTO bill (paid, member_id) VALUES
(true, 1),
(false, 2);

-- Add gym admins
INSERT INTO gym_admin (user_id, admin_first_name, admin_last_name, email, phone, admin_role) VALUES
(3, 'Admin', 'User', 'admin@example.com', '1234567890', 'Administrator');

-- Add gym trainers
INSERT INTO gym_trainer (user_id, first_name, last_name, phone, email, specialization) VALUES
(4, 'Trainer', 'One', '9876543210', 'trainer1@example.com', 'cardio'),
(4, 'Trainer', 'Two', '9876543211', 'trainer2@example.com', 'weights');

-- Add gym schedules
INSERT INTO gym_schedule (available_time, booking_length, trainer_id, day_of_week) VALUES
('08:00:00', '1 hour', 1, 'Monday'),
('09:00:00', '1 hour', 2, 'Tuesday');

-- Add gym rooms
INSERT INTO gym_room (room_name, room_number, room_capacity, room_availability) VALUES
('Cardio Room', 101, 20, true),
('Weight Room', 102, 15, true);

-- Add gym classes
INSERT INTO gym_class (room_id, trainer_id, class_type, category, start_time, end_time, number_of_people, enrollment_limit) VALUES
(1, 1, 'group', 'cardio', '2024-04-13 10:00:00', '2024-04-13 11:00:00', 15, 20),
(2, 2, 'individual', 'weights', '2024-04-14 10:00:00', '2024-04-14 11:00:00', 10, 15);

-- Add gym equipment
INSERT INTO gym_equipment (equipment_name, last_maintained, room_id) VALUES
('Treadmill', '2024-03-01', 1),
('Dumbbells', '2024-03-15', 2);

-- Add booked classes
INSERT INTO booked_classes (member_id, class_id) VALUES
(1, 1),
(2, 2);

-- Add more gym users
INSERT INTO gym_user (user_type, username, user_password) VALUES
('member', 'alice_smith', 'password456'),
('member', 'bob_johnson', 'pass456'),
('trainer', 'trainer3', 'trainer_pass');

-- Add more gym members
INSERT INTO gym_member (user_id, first_name, last_name, phone, email, payment_info, subscription_type, subscription_start, subscription_end, member_weight, member_height, weight_goals, num_workouts_week, calorie_burn_goal, saved_routines) VALUES
(3, 'Alice', 'Smith', '5551234567', 'alice.smith@example.com', 'Credit Card', 'premium', '2023-03-01', '2024-03-01', 140.0, 60.0, 130.0, 4, 600, 'Routine 5, Routine 6'),
(4, 'Bob', 'Johnson', '5559876543', 'bob.johnson@example.com', 'PayPal', 'basic', '2023-04-01', '2024-04-01', 160.0, 65.0, 150.0, 3, 500, 'Routine 7, Routine 8');

-- Add more bills
INSERT INTO bill (paid, member_id) VALUES
(true, 3),
(false, 4);

-- Add more gym admins
INSERT INTO gym_admin (user_id, admin_first_name, admin_last_name, email, phone, admin_role) VALUES
(5, 'Admin', 'User2', 'admin2@example.com', '5551234567', 'Administrator');

-- Add more gym trainers
INSERT INTO gym_trainer (user_id, first_name, last_name, phone, email, specialization) VALUES
(5, 'Trainer', 'Three', '5559876543', 'trainer3@example.com', 'yoga');

-- Add more gym schedules
INSERT INTO gym_schedule (available_time, booking_length, trainer_id, day_of_week) VALUES
('10:00:00', '1 hour', 3, 'Wednesday'),
('11:00:00', '1 hour', 3, 'Thursday');

-- Add more gym rooms
INSERT INTO gym_room (room_name, room_number, room_capacity, room_availability) VALUES
('Yoga Room', 103, 15, true),
('Pool', 104, 30, true);

-- Add more gym classes
INSERT INTO gym_class (room_id, trainer_id, class_type, category, start_time, end_time, number_of_people, enrollment_limit) VALUES
(3, 3, 'group', 'yoga', '2024-04-15 10:00:00', '2024-04-15 11:00:00', 10, 15),
(4, 3, 'individual', 'swimming', '2024-04-16 10:00:00', '2024-04-16 11:00:00', 20, 30);

-- Add more gym equipment
INSERT INTO gym_equipment (equipment_name, last_maintained, room_id) VALUES
('Yoga Mats', '2024-03-10', 3),
('Swimming Floats', '2024-03-20', 4);

-- Add more booked classes
INSERT INTO booked_classes (member_id, class_id) VALUES
(3, 3),
(4, 4);

