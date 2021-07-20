const uploadFile = document.getElementById("main_img");
const uploadPicture_1 = document.getElementById("picture_1");
const uploadPicture_2 = document.getElementById("picture_2");
const uploadPicture_3 = document.getElementById("picture_3");
const uploadPicture_4 = document.getElementById("picture_4");
const uploadPicture_5 = document.getElementById("picture_5");

const uploadBtn = document.getElementById("upload-btn");
const uploadBtnPicture_1 = document.getElementById("upload-picture1");
const uploadBtnPicture_2 = document.getElementById("upload-picture2");
const uploadBtnPicture_3 = document.getElementById("upload-picture3");
const uploadBtnPicture_4 = document.getElementById("upload-picture4");
const uploadBtnPicture_5 = document.getElementById("upload-picture5");

uploadBtn.addEventListener("click", function () {
    uploadFile.click();
    });

uploadBtnPicture_1.addEventListener("click", function () {
    uploadPicture_1.click();
    });

uploadBtnPicture_2.addEventListener("click", function () {
    uploadPicture_2.click();
    });

uploadBtnPicture_3.addEventListener("click", function () {
    uploadPicture_3.click();
    });

uploadBtnPicture_4.addEventListener("click", function () {
    uploadPicture_4.click();
    });

uploadBtnPicture_5.addEventListener("click", function () {
    uploadPicture_5.click();
    });


$('#main_img').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-btn').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });

$('#picture_1').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-picture1').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });


$('#picture_2').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-picture2').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });


$('#picture_3').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-picture3').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });


$('#picture_4').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-picture4').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });


$('#picture_5').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-picture5').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });


$('#main_used_picure').change(function () {
            var input = $(this)[0];
            if (input.files && input.files[0]) {
                if (input.files[0].type.match('image.*')) {
                    var reader = new FileReader();
                    reader.onload = function (e) {
                        $('#upload-btn').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                } else {
                    console.log('ошибка, не изображение');
                }
            } else {
                console.log('хьюстон у нас проблема');
            }
        });


