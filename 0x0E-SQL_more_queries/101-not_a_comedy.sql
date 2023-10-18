-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
    -- tv_genres table contains only one record where name = Comedy
        -- (but the id can be different)
    -- display: tv_shows.title
    -- sorted in ascending order by the show title
    -- You can use a maximum of two SELECT statement

SELECT title
FROM tv_shows
WHERE id NOT IN (SELECT tv_show_genres.show_id
                            FROM tv_show_genres INNER JOIN tv_genres
                                ON tv_show_genres.genre_id = tv_genres.id
                            WHERE tv_genres.name LIKE "Comedy")
ORDER BY title;
