def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # a) Check if all scores are percentage based (0-100)
    for item in data:
        score = item['score']
        if score < 0 or score > 100:
            print(f"Error: Score for assignment '{item['assignment']}' is out of range (0-100).")
            sys.exit(1)

    # b) Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = sum(item['weight'] for item in data)
    formative_weight = sum(item['weight'] for item in data if item['group'].lower() == 'formative')
    summative_weight = sum(item['weight'] for item in data if item['group'].lower() == 'summative')

    if total_weight != 100:
        print(f"Validation Error: Total weight is {total_weight}%, but it should be 100%.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Validation Error: Total Formative weight is {formative_weight}%, but it should be 60%.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Validation Error: Total Summative weight is {summative_weight}%, but it should be 40%.")
        sys.exit(1)

    # c) Calculate the Final Grade and GPA
    formative_items = [i for i in data if i['group'].lower() == 'formative']
    summative_items = [i for i in data if i['group'].lower() == 'summative']

    formative_score = sum(item['score'] * item['weight'] / 100 for item in formative_items)
    summative_score = sum(item['score'] * item['weight'] / 100 for item in summative_items)

    total_grade = formative_score + summative_score
    gpa = (total_grade / 100) * 5.0  # Assuming GPA scale is 5.0

    formative_percentage = (formative_score / formative_weight) * 100
    summative_percentage = (summative_score / summative_weight) * 100

    # d) Determine Pass/Fail status (>= 50% in BOTH categories)
    passed_formative = formative_percentage >= 50
    passed_summative = summative_percentage >= 50
    overall_pass = passed_formative and passed_summative

    # e) Check for failed formative assignments (< 50%)
    #      and determine which one(s) have the highest weight for resubmission.
    resubmission_options = []
    if not overall_pass:
        failed_formatives = [i for i in formative_items if i['score'] < 50]
        if failed_formatives:
            max_weight = max(item['weight'] for item in failed_formatives)
            resubmission_options = [item for item in failed_formatives if item['weight'] == max_weight]

    # f) Print the final decision (PASSED / FAILED) and resubmission options
    print(f"Formative: {formative_score:.2f}/{formative_weight:.0f} ({formative_percentage:.1f}%)")
    print(f"Summative: {summative_score:.2f}/{summative_weight:.0f} ({summative_percentage:.1f}%)")
    print(f"Final Grade: {total_grade:.2f}/100")
    print(f"GPA: {gpa:.2f} / 5.0")
    print(f"\nFinal Status: {'PASSED' if overall_pass else 'FAILED'}")

    if not overall_pass:
        if resubmission_options:
            print("\nEligible for resubmission (failed formative with the highest weight):")
            for item in resubmission_options:
                print(f" - {item['assignment']} (score: {item['score']}, weight: {item['weight']})")
        else:
            print("\nNo failed Formative assignments eligible for resubmission.")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
