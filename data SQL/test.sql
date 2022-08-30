CREATE TABLE IF NOT EXISTS `group_number`
(
	`number` INT,
	`cluster` varchar(255),
	PRIMARY KEY ( `number` )
);

SELECT LEFT
	( g.number, 3 ) AS `group`,
	ROUND( AVG( d.rssi ), 1 ) AS `average rssi`,
	ROUND( AVG( d.snr ), 1 ) AS `average snr` 
FROM
	DATA d
	INNER JOIN group_number g
ON
	LEFT(d.Payload, 3) = g.cluster
GROUP BY
	g.number