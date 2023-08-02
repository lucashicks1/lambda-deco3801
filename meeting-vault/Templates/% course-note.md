# {{title}}


## Meetings
```dataviewjs
const {createButton} = app.plugins.plugins["buttons"]

let h = dv.current().file.folder.toString();
h = h+"/Meetings"

var j = 	dv.pages()
	.where(k => k.file.folder == h)
	.sort(k => k.meeting, 'asc').length;

if (j) {
	j=j+1;
} else {
	j=1
}
const r = ('0' + j.toString()).slice(-2);
const fname = h+"/"+dv.current().file.name+".M"+r

dv.paragraph(createButton({
	app, 
	el: this.container, 
	args: {
		name: "Next meeting: "+j, 
		type: "note("+fname+", split) template", 
		action: "% meeting-note", 
		color: "yellow",
	}
}))
```

```dataview
table WITHOUT ID "[["+file.name+"]]" as meeting, modified AS date, topics
sort meeting
where course = ""+this.file.name+""
```
