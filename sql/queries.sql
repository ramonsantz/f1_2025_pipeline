-- 1. Ranking de Voltas Mais Rápidas
SELECT d.name AS driver_name, f.grand_prix, f.time AS fastest_lap_time
FROM fastest_laps f
JOIN drivers d ON d.id = f.driver_id
ORDER BY f.time ASC;

-- 2. Performance by Race (Approximately)
SELECT d.name AS driver_name, r.track, r.position, r.fastest_lap_time
FROM race_results r
JOIN drivers d ON d.id = r.driver_id
GROUP BY d.name
ORDER BY r.position ASC;

-- 3. Drivers with the Most Points
SELECT d.name AS driver_name, SUM(r.points) AS total_points
FROM race_results r
JOIN drivers d ON d.id = r.driver_id
GROUP BY d.id
ORDER BY total_points DESC;
