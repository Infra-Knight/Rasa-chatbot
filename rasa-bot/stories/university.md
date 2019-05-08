## university_contact
* university_contact{"uni": "university"}
    - utter_university_contact

## university_overview
* university_overview{"uni": "university"}
    - utter_university_overview
    - utter_suggest_yn_study_program
> university_overview

## univeristy_overview_yes
> university_overview
* ans_yes
    - utter_study_program
    
## university_overview_no
> university_overview
* ans_no
    - utter_other_question

## university_history
* university_history{"uni": "university"}
    - utter_university_history
    - utter_suggest_yn_study_program
> university_history
    
## university_history_yes
> university_history
* ans_yes
    - utter_study_program
    
## university_history_no
> university_history
* ans_no
    - utter_other_question

## why_vietnam
* why_vietnam
    - utter_why_vietnam
    - utter_suggest_yn_study_program
> why_vietnam
    
## why_vietnam_yes
> why_vietnam
* ans_yes
    - utter_study_program
    
## why_vietnam_no
> why_vietnam
* ans_no
    - utter_other_question

## international_admission
* international_admission
    - utter_international_admission
    - utter_suggest_yn_international_student_support_overview
> international_admission

## international_admission_yes
> international_admission
* ans_yes
    - utter_international_student_support_overview
    - utter_suggest_after_international_student_support_overview

## international_admission_no
> international_admission
* ans_no
    - utter_other_question

## international_admission_requirement
* international_admission_requirement
    - utter_international_admission_requirement

## international_student_support_overview
* international_student_support_overview
    - utter_international_student_support_overview
    - utter_suggest_after_international_student_support_overview

## international_student_support_visa
* international_student_support_visa
    - utter_international_student_support_visa

## international_student_support_accommodate
* international_student_support_accommodate
    - utter_international_student_support_accommodate

## international_student_support_airport_pickup
* international_student_support_airport_pickup
    - utter_international_student_support_airport_pickup

## bach_khoa_apply
* bach_khoa_apply
    - utter_bach_khoa_apply

## bach_khoa_requirement
* bach_khoa_requirement
    - utter_bach_khoa_requirement

## study_program
* study_program
    - utter_study_program

## pre_university
* pre_university
    - utter_pre_university

## bachelor_overall
* bachelor_overall    
    - utter_bachelor_overall

## dormitory_fee
* dormitory_fee
    - utter_dormitory_fee