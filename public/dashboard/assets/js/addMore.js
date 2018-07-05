var key=5;
var val=5;
function add_fields() {
key++;
val++;
var objTo = document.getElementById('room_fields')
var divtest = document.createElement("div");

divtest.innerHTML = '<div class="col-md-6"><div class="form-group"><label>Key #' +key+ '</label> <input type="text" class="form-control" name="key[]" value="" /></div></div> <div class="col-md-6"><div class="form-group"><label>Value #' +val+ '</label><input type="text" class="form-control" name="value[]" value=""/></div></div> ';
objTo.appendChild(divtest)
}
