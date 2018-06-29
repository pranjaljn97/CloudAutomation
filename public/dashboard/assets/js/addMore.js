var room = 1;
function add_fields() {
room++;
var objTo = document.getElementById('room_fields')
var divtest = document.createElement("div");
divtest.innerHTML = '<div class="label">Room ' + room +':</div><div class="content"><div class="row"><div class="col-md-6"><span>Key: <input type="text" name="key[]" value="" /></span></div><div class="col-md-6"><span>Value: <input type="text" namae="value[]" value=""/></span></div></div></div>';
objTo.appendChild(divtest)
}