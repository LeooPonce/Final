const fullImgBox = document.getElementById("fullImgBox"),
fulImg = document.getElementById("fullImg");

function openFullImg(reference){
	fullImgBox.style.display = "flex"
	fullImg.src = reference
}

function closeImg(){
	fullImgBox.style.display = "none"
}
