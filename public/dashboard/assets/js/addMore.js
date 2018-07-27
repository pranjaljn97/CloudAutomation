
var key=0;
var val=0;

function add_fields() {

key++;
val++;

document.getElementById('total').value = key;

var objTo = document.getElementById('room_fields')
var divtest = document.createElement("div");

divtest.innerHTML = '<div class="col-md-6"><div class="form-group"><label>Key #' +key+ '</label> <input type="text" class="form-control" name="key' +key+ '" /></div></div> <div class="col-md-6"><div class="form-group"><label>Value #'+val+'</label><input type="text" class="form-control"name="value' +val+ '"></div></div> ';

objTo.appendChild(divtest)
}



