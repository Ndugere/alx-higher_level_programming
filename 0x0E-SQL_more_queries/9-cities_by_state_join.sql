-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT c.`id`, c.`name`, (SELECT s.`name` FROM `states` AS s WHERE s.`id` = c.`state_id`) AS state_name
FROM `cities` AS c
ORDER BY c.`id`;
