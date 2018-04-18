var result=parseInt($("#result").html());
console.log(result);
switch(result){
	case 0:{
		console.log("inside switch case section 0");
		$("#resultCard").addClass("bg-success text-white");
		$("#suggestion").html("Keep up with your healthy Lifestyle");
		break;
	}
	case 1:{
		console.log("inside switch case section 1");
		$("#resultCard").addClass("bg-primary text-white");
		$("#suggestion").html("Some minor chanegs in your Lifestyle will improve your health");
		break;
	}
	case 2:{
		console.log("inside switch case section 2");
		$("#resultCard").addClass("bg-info text-white");
		$("#suggestion").html("Consider making some changes to your Lifestyle");
		break;
	}
	case 3:{
		console.log("inside switch case section 3");
		$("#resultCard").addClass("bg-warning text-white");
		$("#suggestion").html("Please change your Lifestyle");
		break;
	}
	case 4:{
		console.log("inside switch case section 4");
		$("#resultCard").addClass("bg-danger text-white");
		$("#suggestion").html("Please consult a Doctor immediately !");
		break;
	}
	default:{
		console.log("inside switch case default section");
		break;
	}
}