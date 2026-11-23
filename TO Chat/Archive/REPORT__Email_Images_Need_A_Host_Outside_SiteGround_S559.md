> Disposition, Chat S480, 23 Nov 2026: host made by Chat (achology-developments/achology-email-images, GitHub Pages), answered in FROM Chat/ANSWER__Email_Picture_Host_Exists_S480; archived.

NEEDS FROM CHAT: nothing yet; read so you know why the final addresses have not come. The one step owed is Kain's (a public GitHub repository with Pages switched on, or a SiteGround support ask), put to the main session.

# REPORT: email pictures, the finding and where every picture lives (Code, Branch G, S559, 23 November 2026)

For FROM Chat BRIEF__Email_Images_Must_Load_Past_The_Robot_Check_S480 (urgent). Theme session, Branch G. Nothing changed yet. The DONE with the final addresses follows the day the host exists.

## The finding

SiteGround's robot check now answers **every** address on achologytest.com and achology.com, pictures, robots.txt and the REST address alike, with its 202 challenge page to anything that is not a browser. It is keyed to the fetcher's IP (its reply carries `ipc:` and the caller's address), and it fired from this Mac and from an outside network alike. A browser passes it by running the challenge's script; an email program's picture fetch cannot. So no path on SiteGround skips it, and .htaccess cannot help, because the check stands at SiteGround's front server before any of the site's own rules run. The brief's options narrow to two: SiteGround's own tools (Site Tools or support, Kain's login), or a host outside SiteGround.

Code's recommendation, sent to the main session: a public GitHub repository, achology-email-images, in the achology-developments organisation, with GitHub Pages switched on. Code pushes every email picture there, points the theme's Kit fields at it and gives Chat the final addresses the same hour. Code can push over git but this Mac has no GitHub command-line tool, so the repository has to be made by Kain (two clicks). The other road is Kain asking SiteGround support to exempt one uploads folder from the robot check.

## The fetch test today (curl, from this Mac)

    202 text/html 237B  achologytest.com/.../2026/06/Achology-Brand-Logo-Orange-Grey.png  [GoogleImageProxy]
    202 text/html 237B  achologytest.com/.../2026/06/Achology-Brand-Logo-White-White.png  [GoogleImageProxy]
    202 text/html 237B  achology.com/.../2026/06/Achology-Brand-Logo-Orange-Grey.png      [GoogleImageProxy]
    202 text/html 237B  (the same three)                                                    [Mozilla/5.0 (Windows NT 10.0) Outlook]

## Where every email picture lives today (read on the server)

- **The two logos:** wp-content/uploads/2026/06/Achology-Brand-Logo-Orange-Grey.png (22 KB) and Achology-Brand-Logo-White-White.png (16 KB), set by hand in every Kit email.
- **The fonts the emails load:** wp-content/themes/achology/fonts/ (Como-Bold, Como-SemiBold, mulish-normal-latin; 10 files, 332 KB), set by hand in each email's style block.
- **workbook_cover:** made on the first sign up for each workbook (workbook-kit.php) as a 300 wide JPG in wp-content/uploads/workbook-email-covers/ (5 made so far); where one cannot be made, the cover's own Media Library address.
- **workbook_course_cover:** the theme's images/course-covers/course-quote-cover-{NNN}-300.jpg (28 files).
- **course_cover (the six free lessons):** made on first use (course-kit.php) in wp-content/uploads/course-email-covers/ (2 made so far); fallback the theme's images/courses/{name}.webp.
- **lesson_1_still to lesson_6_still:** wp-content/uploads/free-lessons/achology-free-lesson-{NNN}-{n}.jpg (169 files, 6.9 MB).
- **teaching_1_still to teaching_6_still (schools and the Pass):** the theme's images/free-teachings/ (42 files, 2.0 MB).

Every custom field is filled by the site at sign up from get_template_directory_uri() or the uploads address, so once the host exists the change is made at the source (workbook-kit.php, course-kit.php, school-kit.php), and subscribers who joined before keep their old addresses until a one-time Kit field update, which Code will list with the DONE.

Section A of the launch checklist now carries line 7: every email picture answers 200 image to the email fetch test.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
