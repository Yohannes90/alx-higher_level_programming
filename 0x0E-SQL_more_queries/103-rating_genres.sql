-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
    -- display: tv_genres.name - rating sum
    -- sorted in descending order by their rating
    -- You can use only one SELECT statement

SELECT name, SUM(rate) AS rating
FROM tv_show_genres INNER JOIN tv_show_ratings
    ON tv_show_genres.show_id = tv_show_ratings.show_id INNER JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
GROUP BY name
ORDER BY rating DESC;
