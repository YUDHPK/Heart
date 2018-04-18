$(document).ready(function(){
	$("#l2").hide();
	$("#l3").hide();
	$("#l4").hide();
	$("#l5").hide();
	$("#l6").hide();
	$("#l7").hide();
	$("#l8").hide();
	$("#l9").hide();
	$("#l10").hide();
});

$("input[name='q1']").on("change",function(attribute) {
	//console.log(2)
	$("#l2").show();
});

$("input[name='q2']").on("change",function(attribute) {
	//console.log(2)
	$("#l3").show();
});

$("input[name='q3']").on("change",function(attribute) {
	//console.log(2)
	$("#l4").show();
});

$("input[name='q4']").on("change",function(attribute) {
	//console.log(2)
	$("#l5").show();
});

$("input[name='q5']").on("change",function(attribute) {
	//console.log(2)
	$("#l6").show();
});

$("input[name='q6']").on("change",function(attribute) {
	//console.log(2)
	$("#l7").show();
});

$("input[name='q7']").on("change",function(attribute) {
	//console.log(2)
	$("#l8").show();
});

$("input[name='q8']").on("change",function(attribute) {
	//console.log(2)
	$("#l9").show();
});

$("input[name='q9']").on("change",function(attribute) {
	//console.log(2)
	$("#l10").show();
});

function saveModal(){
	var v = parseInt($("input[name='q1']:checked").val());
	v+=parseInt($("input[name='q2']:checked").val());
	v+=parseInt($("input[name='q3']:checked").val());
	v+=(4-parseInt($("input[name='q4']:checked").val()));
	v+=(4-parseInt($("input[name='q5']:checked").val()));
	v+=parseInt($("input[name='q6']:checked").val());
	v+=(4-parseInt($("input[name='q7']:checked").val()));
	v+=(4-parseInt($("input[name='q8']:checked").val()));
	v+=parseInt($("input[name='q9']:checked").val());
	v+=parseInt($("input[name='q10']:checked").val());
	$("#stress").val(v);
	console.log(v);
	$("#qModal").modal('hide');
	$("#checkButton").click();
}

$("input[name='q10']").on("change",saveModal);

$('#modalSave').click(saveModal);

function submitAdvice(z) {
	// body...
	//alert("Vsv");
	return true;
}

$("#checkButton").click(function(){
	var name=$("#client").val();
	console.log("Name",name);

	var age=parseInt($("#age").val());
	console.log("Age",age);

	var sex=parseInt($("#sex").val());
	console.log("Gender",sex);

	var chestPain=parseInt($("#chestPain").val());
	console.log("Chest Pain",chestPain);

	var restingBP=parseInt($("#restingBP").val());
	console.log("Resting BP",restingBP);

	var cholestrol=parseInt($("#cholestrol").val());
	console.log("Cholestrol",cholestrol);

	var diabetes=parseInt($("#diabetes").val());
	console.log("Diabetes",diabetes);

	var smokingLevel=parseInt($("#smokingLevel").val());
	console.log("Smoking Level",smokingLevel);

	var maxHeartRate=parseInt($("#maxHeartRate").val());
	console.log("Max Heart Rate",maxHeartRate);

	var exerciseLevel=parseInt($("#exerciseLevel").val());
	console.log("Exercise Level",exerciseLevel);

	var weight=parseFloat($("#weight").val());
	console.log("Weight",weight);

	var height=parseFloat($("#height").val());
	console.log("Height",height);

	var bmi=weight/height/height;
	bmi=Math.trunc(bmi);
	console.log("Bmi",bmi)
	
	var alcoholLevel=parseInt($("#alcoholLevel").val());
	console.log("Alcohol Level",alcoholLevel);

	var stress=parseInt($("#stress").val());
	console.log("Stress",stress);

	var data=[name,age,sex,chestPain,restingBP,cholestrol,diabetes,smokingLevel,maxHeartRate,exerciseLevel,bmi,alcoholLevel,stress];
	console.log(data);

	dataJson=JSON.stringify(data);
	$("#elements").val(dataJson);
});
