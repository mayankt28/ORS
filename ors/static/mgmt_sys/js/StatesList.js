
var state_arr = new Array("Assam", "Bihar", "Delhi", "Gujarat", "Maharashtra", "Rajasthan", "Tamil Nadu", "Uttar Pradesh", "West Bengal");


var Hospital_Arr = new Array();

Hospital_Arr[0] = "";
Hospital_Arr[1] = "Gauhati Medical College and Hospital|Lions Eye Hospital|Assam Medical College and Hospital|Silchar Medical College and Hospital";
Hospital_Arr[2] = "Jawaharlal Nehru Medical College and Hospital|Darbhanga Medical College and Hospital|Mithila Minority Dental College and Hospital|Katihar Medical College|Sri Krishna Medical College|Guru Gobind Singh Hospital, Patna Sahib|AIIMS Patna";
Hospital_Arr[3] = "All India Institute of Medical Sciences, Ansari Nagar|Sanjeevan Hospitals|Vidyasagar Institute of Mental Health and Neuro Sciences|World Laparoscopy Hospital, Gurgaon|Fortis Hospital, Gurgaon|Maulana Azad Medical College, Bahadur Shah Zafar Marg|Kasturba Hospital";
Hospital_Arr[4] = "Ahmedabad Civil Hospital|Ganga Ram Hospital|World Laparoscopy Hospital|Muljibhai Patel Urological Hospital";
Hospital_Arr[5] = "Bhabha Hospital, Bandra|Cooper Hospital, Vile Parle|Shushrusha Citizens' Co-operative Hospital|Tata Memorial Hospital|Mahatma Gandhi Memorial Hospital|Aditya Birla Memorial Hospital|Shri Vasantrao Naik Government Medical College";
Hospital_Arr[6] = "Mathura Das Mathur Hospital, Jodhpur";
Hospital_Arr[7] = "Apollo Hospitals, Greams Road|Fortis Malar Hospital|Sri Ramachandra Medical College and Research Institute|PSG Institute of Medical Sciences & Research|Government Vellore Medical College Hospital";
Hospital_Arr[8] = "Jawaharlal Nehru Medical College|Ganesh Shankar Vidyarthi Memorial Medical College|Dr. Mohan’s Diabetes Specialities Centre|Sir Sunderlal Hospital (IMS BHU)";
Hospital_Arr[9] = "Columbia Asia Hospital, Salt Lake|Nil Ratan Sarkar Medical College and Hospital|Peerless Hospital|R. G. Kar Medical College and Hospital|The Mission Hospital, Durgapur|Nightingale Nursing Home";



var Dept_Arr = new Array();

Dept_Arr[0] = "";
Dept_Arr[1] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[2] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[3] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[4] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[5] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[6] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[7] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[8] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[9] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[10] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[11] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";
Dept_Arr[12] = "Orthopaedics|Oncology|cardiology|gastroenterology|diabetology|metabolism|nephrology|vascular diseases|pancreas";



function populateStates(StatesElementId, HospitalElementId , DepartmentElementId){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var StatesElement = document.getElementById(StatesElementId);
	StatesElement.length=0;
	StatesElement.options[0] = new Option('Select State','-1');
	StatesElement.options[0].setAttribute('disabled','disabled');
	StatesElement.options[0].setAttribute('selected','selected');

	StatesElement.selectedIndex = 0;
	for (var i=0; i<state_arr.length; i++) {
		StatesElement.options[StatesElement.length] = new Option(state_arr[i],state_arr[i]);
	}

	// Assigned all countries. Now assign event listener for the states.

	if( HospitalElementId ){
		StatesElement.onchange = function(){
			populateHospitals( StatesElementId, HospitalElementId ,DepartmentElementId);
			populateDepartments( HospitalElementId ,DepartmentElementId);
		};	
	}
}

function populateHospitals( StateElementId, HospitalElementId, DepartmentElementId){
	
	var selectedStateIndex = document.getElementById( StateElementId ).selectedIndex;

	var HospitalElement = document.getElementById( HospitalElementId );
	
	HospitalElement.length=0;	// Fixed by Julian Woods
	HospitalElement.selectedIndex = 0;
	HospitalElement.options[0] = new Option('Select Hospital','-1');
	HospitalElement.options[0].setAttribute('disabled','disabled');
	HospitalElement.options[0].setAttribute('selected','selected');


	var Hospital_arr = Hospital_Arr[selectedStateIndex].split("|");
	
	for (var i=0; i<Hospital_arr.length; i++) {
		HospitalElement.options[HospitalElement.length] = new Option(Hospital_arr[i],Hospital_arr[i]);
	}


	if( DepartmentElementId ){
		HospitalElement.onchange = function(){
			populateDepartments( HospitalElementId ,DepartmentElementId);
		};
	}
}

function populateDepartments(HospitalElementId , DepartmentElementId){
	
	var selectedHospitalIndex = document.getElementById( HospitalElementId ).selectedIndex;

	var DepartmentElement = document.getElementById( DepartmentElementId );
	
	DepartmentElement.length=0;	// Fixed by Julian Woods
	DepartmentElement.selectedIndex = 0;
	DepartmentElement.options[0] = new Option('Select Department','-1');
	DepartmentElement.options[0].setAttribute('disabled','disabled');
	DepartmentElement.options[0].setAttribute('selected','selected');

	var Department_Arr = Dept_Arr[selectedHospitalIndex].split("|");
	
	for (var i=0; i<Department_Arr.length; i++) {
		DepartmentElement.options[DepartmentElement.length] = new Option(Department_Arr[i],Department_Arr[i]);
	}
}