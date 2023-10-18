-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
    -- tv_shows table contains only one record where title = Dexter
        -- (but the id can be different)
    -- display: tv_genres.name
    -- sorted in ascending order by the genre name
    -- You can use a maximum of two SELECT statement

SELECT name
FROM tv_genres
WHERE id NOT IN (SELECT tv_show_genres.genre_id
                            FROM tv_show_genres INNER JOIN tv_shows
                                ON tv_show_genres.show_id = tv_shows.id
                            WHERE tv_shows.title LIKE "Dexter")
ORDER BY name;
