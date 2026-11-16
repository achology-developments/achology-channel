> CHAT DISPOSITION, S470: READ. Ship brief; nothing owed.

DONE: nothing needed from Chat. A ship brief, for Chat's picture of the build.

# The Schools, Courses, People and Policies admin tabs show their Rank Math columns (0.708.101)

**What Kain saw.** On the Courses tab every row read N/A, "Keyword: Not Set", and the default title and description. He asked why the Rank Math score was not showing.

**What was true.** The fields were stored all along. Read off the install for the Diploma (post 33506): score 91, its signed title and description, its focus phrase with five related phrases. Only the Diploma was read, not the other 27.

**The cause.** Each of the four tabs lists child pages whose parents are not in the list. With no sort in the request, WordPress lists Pages as a tree, and Rank Math's list columns then gather their fields by walking down from the top-level pages. A list of children alone has no top-level page, so nothing was gathered and the blanks were printed.

**The mend.** The theme's admin file now puts the title sort into the request itself for those four tabs, before WordPress or Rank Math reads it. The list is a plain list sorted by title, as it already looked, and the columns fill. A sort chosen by clicking a column heading is left alone. Kain asked for all four tabs in one go.

**Not proved by Code.** The file parses on the server and is deployed. The tab itself was not opened by Code in a signed-in browser; Kain was asked to reload it and say what he sees.

**A correction to the course page record, for Chat.** The scores table of 11 November (71 to 84) is the reading before the score lift. The stored score for the Diploma today is 91.

*No em or en dashes in this file; checked before writing.*
