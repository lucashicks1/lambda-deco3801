<%*
  let title = tp.file.title;
  var course = title.slice(0,-4);
  var meeting = title.slice(-2);
  meeting = Number(meeting);
%>
---
created: <% tp.file.creation_date("YYYY-MM-DDTHH:mm:ss") %>
modified: <% tp.file.last_modified_date("YYYY-MM-DDTHH:mm:ss") %>
course: <%* tR += `${course}` %>
tags: [meeting]
topics:
 - <% tp.file.cursor(2) %>
---
# <%* tR += `${course}` %> Meeting <%* tR += `${meeting}` %>
- [i] course:: [[<%* tR += `${course}` %>]]
- [i] date:: <% tp.file.creation_date("YYYY-MM-DDTHH:mm:ss") %>
- [i] meeting:: <%* tR += `${meeting}` %>

# <% tp.file.cursor(1) %>


---
