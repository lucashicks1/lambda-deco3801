export const TIME_DELTA = 0;
export const TIMESLOT_LEN = 30;
export const FAMILY_NAME = "family";
export const USERS = ["user_1", "user_2", "user_3", "user_4", FAMILY_NAME];
export const DAYS = ["sunday", "monday", "tuesday", "wednesday", 
"thursday", "friday", "saturday"]; // ECMAScript ordering
// Dictionary for readable conversions between ECMAScript Date format 
// (begins on Sunday) and app calendar (begins on Monday)
// TODO this might be something we set in the config file?
export const DAY_POSITIONS = {"monday": 0, "tuesday": 1, 
"wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6};
