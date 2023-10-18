-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
    -- If a show doesn’t have a genre, display NULL in the genre column
    -- display: tv_shows.title - tv_genres.name
    -- sorted in ascending order by the show title and genre name
    -- You can use only one SELECT statement

SELECT tv_shows.title, tv_genres.name
FROM tv_genres LEFT JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id RIGHT JOIN tv_shows
        ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name;
