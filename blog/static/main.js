src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"

var bio_area = document.getElementById('bio_area');
var bio_count = document.getElementById('bio_count');

var targets_area = document.getElementById('targets_area');
var targets_count = document.getElementById('targets_count');

var description_area = document.getElementById('description_area');
var description_count = document.getElementById('description_count');

var title_area = document.getElementById('title_area');
var title_count = document.getElementById('title_count');

var fileInput = document.getElementById('file-input');
var imagePreview = document.getElementById('image-preview');

var isOpened = false;

var selectedFiles = [];
var counter = 0;

var filesInput = document.getElementById('files-input');
var mainImageForPost = document.getElementById('main-for-post');

function deleteImage(id , array) {
    array.splice(id , 1);
}

if(bio_area) {
    bio_area.addEventListener('input', function() {
    var text = this.value;
    var maxLength = this.maxLength;
    var currentLength = text.length;

    bio_count.textContent = currentLength + ' / ' + maxLength + ' symbols';
});
}

if(description_area) {
    description_area.addEventListener('input', function() {
    var text = this.value;
    var maxLength = this.maxLength;
    var currentLength = text.length;

    description_count.textContent = currentLength + ' / ' + maxLength + ' symbols';
});
}

if(title_area) {
    title_area.addEventListener('input', function() {
    var text = this.value;
    var maxLength = this.maxLength;
    var currentLength = text.length;

    title_count.textContent = currentLength + ' / ' + maxLength + ' symbols';
});
}

if(bio_area) {
    bio_area.addEventListener('input', function() {
    var text = this.value;
    var maxLength = this.maxLength;
    var currentLength = text.length;

    bio_count.textContent = currentLength + ' / ' + maxLength + ' symbols';
});
}

if(fileInput) {
    fileInput.addEventListener('change', function() {
    var file = fileInput.files[0];

    if (file) {
        var reader = new FileReader();

        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        };

        reader.readAsDataURL(file);
    }
});
}
function showFormForPost() {
    var postForm = document.getElementById('postForm');
    if(isOpened == false) {
        postForm.style.display = 'block';
        isOpened = true;
    }
    else{
        postForm.style.display = 'none';
        isOpened = false;
    }
}

document.getElementById('files-input').addEventListener('change', function () {

    var files = this.files;
    if (files.length > 10 || selectedFiles.length > 10) {
        alert('You can select up to 10 files.');
        this.value = '';
        return;
    }

    for (var i = 0; i < files.length; i++) {
        selectedFiles.push(files[i]);
    }
    return selectedFiles;
});

if(filesInput) {
    filesInput.addEventListener('change', function() {
    updateImageContainer();
    var imageContainer = document.getElementById('all-images-for-post');

    while(counter != selectedFiles.length) {
        console.log(selectedFiles)
        if(counter == 0){
            var img = document.getElementById('main-for-post');
            img.src = URL.createObjectURL(selectedFiles[counter]);
            img.id = counter;
            img.addEventListener('click', function () {
                    deleteImage(this.id, selectedFiles);
                    updateImageContainer();
                });
        }
        else {
            var img = document.createElement('img');
            img.src = URL.createObjectURL(selectedFiles[counter]);
            img.classList.add('images_for_post');
            img.classList.add('center_horizont');
            img.id = counter;
            imageContainer.appendChild(img);
            img.addEventListener('click', function () {
                    deleteImage(this.id, selectedFiles);
                    updateImageContainer();
                });
        }
        counter++;
    }
});
}

function updateImageContainer() {
    var imageContainer = document.getElementById('all-images-for-post');
    imageContainer.innerHTML = '';

    for (var i = 0; i < selectedFiles.length; i++) {
        var img = document.createElement('img');
        img.src = URL.createObjectURL(selectedFiles[i]);
        img.classList.add('images_for_post');
        img.classList.add('center_horizont');
        img.id = i;

        img.addEventListener('click', function () {
            deleteImage(this.id, selectedFiles);
            updateImageContainer();
        });

        imageContainer.appendChild(img);
    }
}

function IsPostLiked(post_id, callback) {
    $.ajax({
        url: "/blog/is_post_liked",
        headers: { 'X-CSRFToken': csrftoken },
        type: "POST",
        data: {
            post_id: post_id
        },
        success: function (data, textStatus, jqXHR) {
            callback(data);
        },
        error: function (jqXHR, textStatus, errorThrown) {

        }
    });
}