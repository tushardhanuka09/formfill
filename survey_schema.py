"""
Survey Schema Definition for AcSIR Societal Program Survey:
Screen Use Behaviour, Digital Habits and Visual Well-being
"""

SURVEY_METADATA = {
    "title_en": "Screen Use Behaviour, Digital Habits and Visual Well-being",
    "title_hi": "स्क्रीन उपयोग व्यवहार, डिजिटल आदतें और दृश्य कल्याण (विज़ुअल वेल-बीइंग)",
    "program_en": "Societal Program: Problem Understanding and Analysis (AcSIR-04-SP)",
    "instructions_en": "This survey aims to understand patterns of digital-device use, continuous screen exposure, night-time device use, visual habits, sleep-related behavior, concentration, and strategies used to manage screen exposure.",
    "instructions_hi": "इस सर्वेक्षण का उद्देश्य डिजिटल डिवाइस के उपयोग के पैटर्न, निरंतर स्क्रीन एक्सपोज़र, रात में डिवाइस के उपयोग, दृश्य आदतों, नींद से संबंधित व्यवहार, एकाग्रता और स्क्रीन एक्सपोज़र को प्रबंधित करने के लिए उपयोग की जाने वाली रणनीतियों को समझना है।"
}

SECTIONS = [
    {
        "id": "section1",
        "title_en": "SECTION 1 — PARTICIPANT INFORMATION",
        "title_hi": "अनुभाग 1 — प्रतिभागी जानकारी",
        "question_ids": ["q1", "q2", "q3"]
    },
    {
        "id": "section2",
        "title_en": "SECTION 2 — DAILY SCREEN-USE PATTERN",
        "title_hi": "अनुभाग 2 — दैनिक स्क्रीन-उपयोग पैटर्न",
        "question_ids": ["q4", "q5", "q6"]
    },
    {
        "id": "section3",
        "title_en": "SECTION 3 — CONTINUOUS SCREEN EXPOSURE AND VISUAL HABITS",
        "title_hi": "अनुभाग 3 — निरंतर स्क्रीन एक्सपोज़र और दृश्य आदतें",
        "question_ids": ["q7", "q8", "q9", "q10", "q11", "q12"]
    },
    {
        "id": "section4",
        "title_en": "SECTION 4 — NIGHT-TIME DIGITAL BEHAVIOUR",
        "title_hi": "अनुभाग 4 — रात के समय डिजिटल व्यवहार",
        "question_ids": ["q13", "q14", "q15", "q16", "q17"]
    },
    {
        "id": "section5",
        "title_en": "SECTION 5 — CONCENTRATION AND DAILY FUNCTIONING",
        "title_hi": "अनुभाग 5 — एकाग्रता और दैनिक कार्यप्रणाली",
        "question_ids": ["q18", "q19", "q20"]
    },
    {
        "id": "section6",
        "title_en": "SECTION 6 — AWARENESS AND PREVENTIVE PRACTICES",
        "title_hi": "अनुभाग 6 — जागरूकता और निवारक उपाय",
        "question_ids": ["q21", "q22", "q23"]
    }
]

QUESTIONS = [
    # --- SECTION 1 ---
    {
        "id": "q1",
        "number": 1,
        "type": "radio",
        "required": True,
        "text_en": "What is your age group?",
        "text_hi": "आपकी आयु वर्ग क्या है?",
        "options": [
            {"value": "18-22", "text_en": "18–22 years", "text_hi": "18–22 वर्ष", "page": 2, "box_idx": 0},
            {"value": "23-27", "text_en": "23–27 years", "text_hi": "23–27 वर्ष", "page": 2, "box_idx": 1},
            {"value": "28-32", "text_en": "28–32 years", "text_hi": "28–32 वर्ष", "page": 2, "box_idx": 2},
            {"value": "33_plus", "text_en": "33 years or above", "text_hi": "33 वर्ष या उससे अधिक", "page": 2, "box_idx": 3},
            {"value": "pnd", "text_en": "Prefer not to disclose", "text_hi": "ख़ुलासा न करना पसंद करेंगे", "page": 2, "box_idx": 4}
        ]
    },
    {
        "id": "q2",
        "number": 2,
        "type": "radio",
        "required": True,
        "text_en": "What is your gender?",
        "text_hi": "आपका लिंग क्या है?",
        "options": [
            {"value": "male", "text_en": "Male", "text_hi": "पुरुष", "page": 2, "box_idx": 5},
            {"value": "female", "text_en": "Female", "text_hi": "महिला", "page": 2, "box_idx": 6},
            {"value": "other", "text_en": "Other", "text_hi": "अन्य", "page": 2, "box_idx": 7},
            {"value": "pnd", "text_en": "Prefer not to disclose", "text_hi": "ख़ुलासा न करना पसंद करेंगे", "page": 2, "box_idx": 8}
        ]
    },
    {
        "id": "q3",
        "number": 3,
        "type": "radio",
        "required": True,
        "text_en": "What is your current living arrangement?",
        "text_hi": "आपकी वर्तमान रहने की व्यवस्था क्या है?",
        "options": [
            {"value": "alone", "text_en": "Living alone", "text_hi": "अकेले रहना", "page": 2, "box_idx": 9},
            {"value": "parents", "text_en": "Living with parents/family", "text_hi": "माता-पिता/परिवार के साथ रहना", "page": 2, "box_idx": 10},
            {"value": "partner", "text_en": "Living with spouse/partner", "text_hi": "जीवनसाथी/पार्टनर के साथ रहना", "page": 2, "box_idx": 11},
            {"value": "roommates", "text_en": "Living with roommates/peers", "text_hi": "रूममेट्स/साथियों के साथ रहना", "page": 2, "box_idx": 12},
            {"value": "hostel", "text_en": "Hostel/residential accommodation", "text_hi": "हॉस्टल/आवासीय आवास", "page": 2, "box_idx": 13},
            {"value": "other", "text_en": "Other", "text_hi": "अन्य", "page": 2, "box_idx": 14}
        ]
    },

    # --- SECTION 2 ---
    {
        "id": "q4",
        "number": 4,
        "type": "radio",
        "required": True,
        "text_en": "On a typical day, approximately how many total hours do you spend using digital screens for all purposes?",
        "text_hi": "एक सामान्य दिन में, आप सभी उद्देश्यों के लिए डिजिटल स्क्रीन का उपयोग करने में कुल कितने घंटे बिताते हैं?",
        "options": [
            {"value": "lt3", "text_en": "Less than 3 hours", "text_hi": "3 घंटे से कम", "page": 3, "box_idx": 0},
            {"value": "3-5", "text_en": "3–5 hours", "text_hi": "3–5 घंटे", "page": 3, "box_idx": 1},
            {"value": "5-7", "text_en": "5–7 hours", "text_hi": "5–7 घंटे", "page": 3, "box_idx": 2},
            {"value": "7-9", "text_en": "7–9 hours", "text_hi": "7–9 घंटे", "page": 3, "box_idx": 3},
            {"value": "10_plus", "text_en": "10 hours or more", "text_hi": "10 घंटे या उससे अधिक", "page": 3, "box_idx": 4}
        ]
    },
    {
        "id": "q5",
        "number": 5,
        "type": "radio",
        "required": True,
        "text_en": "During a typical weekday, during which period do you spend the most time using digital screens?",
        "text_hi": "एक सामान्य कार्यदिवस के दौरान, आप किस अवधि में डिजिटल स्क्रीन का उपयोग करने में सबसे अधिक समय बिताते हैं?",
        "options": [
            {"value": "morning", "text_en": "Morning (6 AM–12 PM)", "text_hi": "सुबह (सुबह 6 बजे से दोपहर 12 बजे तक)", "page": 3, "box_idx": 5},
            {"value": "afternoon", "text_en": "Afternoon (12 PM–5 PM)", "text_hi": "दोपहर (दोपहर 12 बजे से शाम 5 बजे तक)", "page": 3, "box_idx": 6},
            {"value": "evening", "text_en": "Evening (5 PM–9 PM)", "text_hi": "शाम (शाम 5 बजे से रात 9 बजे तक)", "page": 3, "box_idx": 7},
            {"value": "latenight", "text_en": "Late night (after 9 PM)", "text_hi": "देर रात (रात 9 बजे के बाद)", "page": 3, "box_idx": 8},
            {"value": "distributed", "text_en": "Screen use is fairly evenly distributed throughout the day", "text_hi": "स्क्रीन का उपयोग पूरे दिन समान रूप से वितरित रहता है", "page": 3, "box_idx": 9}
        ]
    },
    {
        "id": "q6",
        "number": 6,
        "type": "radio",
        "required": True,
        "text_en": "What is your most common reason for using a digital screen for non-academic/non-work purposes?",
        "text_hi": "गैर-शैक्षणिक/गैर-कार्य उद्देश्यों के लिए डिजिटल स्क्रीन का उपयोग करने का आपका सबसे सामान्य कारण क्या है?",
        "options": [
            {"value": "social", "text_en": "social media / messaging / chatting", "text_hi": "सोशल मीडिया / मैसेजिंग / चैटिंग", "page": 3, "box_idx": 10},
            {"value": "videos", "text_en": "Watching videos / movies / streaming", "text_hi": "वीडियो / फिल्में देखना / स्ट्रीमिंग", "page": 3, "box_idx": 11},
            {"value": "gaming", "text_en": "Online gaming", "text_hi": "ऑनलाइन गेमिंग", "page": 3, "box_idx": 12},
            {"value": "browsing", "text_en": "Browsing / news / general internet use", "text_hi": "ब्राउज़िंग / समाचार / सामान्य इंटरनेट उपयोग", "page": 3, "box_idx": 13},
            {"value": "shopping", "text_en": "Online shopping", "text_hi": "ऑनलाइन शॉपिंग", "page": 3, "box_idx": 14},
            {"value": "other", "text_en": "Other", "text_hi": "अन्य", "page": 3, "box_idx": 15}
        ]
    },

    # --- SECTION 3 ---
    {
        "id": "q7",
        "number": 7,
        "type": "radio",
        "required": True,
        "text_en": "How often do you check your smartphone when you do not have a specific task or notification requiring you to do so?",
        "text_hi": "जब आपके पास ऐसा करने के लिए कोई विशिष्ट कार्य या सूचना (नोटिफिकेशन) नहीं होती है, तब आप कितनी बार अपना स्मार्टफोन चेक करते हैं?",
        "options": [
            {"value": "never", "text_en": "Rarely or never", "text_hi": "शायद ही कभी या कभी नहीं", "page": 4, "box_idx": 0},
            {"value": "occasionally", "text_en": "Occasionally", "text_hi": "कभी-कभार", "page": 4, "box_idx": 1},
            {"value": "several", "text_en": "Several times a day", "text_hi": "दिन में कई बार", "page": 4, "box_idx": 2},
            {"value": "frequently", "text_en": "Frequently throughout the day", "text_hi": "पूरे दिन बार-बार", "page": 4, "box_idx": 3},
            {"value": "continuously", "text_en": "Almost continuously", "text_hi": "लगभग लगातार", "page": 4, "box_idx": 4}
        ]
    },
    {
        "id": "q8",
        "number": 8,
        "type": "radio",
        "required": True,
        "text_en": "How often does your recreational screen use continue longer than you originally intended?",
        "text_hi": "आपका मनोरंजक स्क्रीन उपयोग आपकी मूल मंशा से अधिक समय तक कितनी बार जारी रहता है?",
        "options": [
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 4, "box_idx": 5},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 4, "box_idx": 6},
            {"value": "sometimes", "text_en": "Sometimes", "text_hi": "कभी-कभी", "page": 4, "box_idx": 7},
            {"value": "often", "text_en": "Often", "text_hi": "अक्सर", "page": 4, "box_idx": 8},
            {"value": "always", "text_en": "Almost always", "text_hi": "लगभग हमेशा", "page": 4, "box_idx": 9}
        ]
    },
    {
        "id": "q9",
        "number": 9,
        "type": "radio",
        "required": True,
        "text_en": "What is the longest period you usually spend continuously looking at a screen without taking a meaningful break?",
        "text_hi": "बिना कोई सार्थक ब्रेक लिए आप आमतौर पर स्क्रीन को लगातार देखने में सबसे लंबा कितना समय बिताते हैं?",
        "options": [
            {"value": "lt30m", "text_en": "Less than 30 minutes", "text_hi": "30 मिनट से कम", "page": 4, "box_idx": 10},
            {"value": "30-60m", "text_en": "30–60 minutes", "text_hi": "30–60 मिनट", "page": 4, "box_idx": 11},
            {"value": "1-2h", "text_en": "1–2 hours", "text_hi": "1–2 घंटे", "page": 4, "box_idx": 12},
            {"value": "2-3h", "text_en": "2–3 hours", "text_hi": "2–3 घंटे", "page": 4, "box_idx": 13},
            {"value": "gt3h", "text_en": "More than 3 hours", "text_hi": "3 घंटे से अधिक", "page": 4, "box_idx": 14}
        ]
    },
    {
        "id": "q10",
        "number": 10,
        "type": "radio",
        "required": True,
        "text_en": "How often do you use a digital screen in a dark or poorly lit environment?",
        "text_hi": "आप अँधेरे या कम रोशनी वाले वातावरण में डिजिटल स्क्रीन का उपयोग कितनी बार करते हैं?",
        "options": [
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 4, "box_idx": 15},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 5, "box_idx": 0},
            {"value": "sometimes", "text_en": "Sometimes", "text_hi": "कभी-कभी", "page": 5, "box_idx": 1},
            {"value": "often", "text_en": "Often", "text_hi": "अक्सर", "page": 5, "box_idx": 2},
            {"value": "almost_daily", "text_en": "Almost every day", "text_hi": "लगभग हर दिन", "page": 5, "box_idx": 3}
        ]
    },
    {
        "id": "q11",
        "number": 11,
        "type": "radio",
        "required": True,
        "text_en": "How often do you deliberately look away from the screen or take a visual break during prolonged screen use?",
        "text_hi": "लंबे समय तक स्क्रीन के उपयोग के दौरान आप कितनी बार जानबूझकर स्क्रीन से दूर देखते हैं या आँखों को आराम देने के लिए ब्रेक लेते हैं?",
        "options": [
            {"value": "20-30m", "text_en": "Every 20–30 minutes", "text_hi": "हर 20–30 मिनट में", "page": 5, "box_idx": 4},
            {"value": "30-60m", "text_en": "Every 30–60 minutes", "text_hi": "हर 30–60 मिनट में", "page": 5, "box_idx": 5},
            {"value": "after_task", "text_en": "Only after completing a task", "text_hi": "कार्य पूरा करने के बाद ही", "page": 5, "box_idx": 6},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 5, "box_idx": 7},
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 5, "box_idx": 8}
        ]
    },
    {
        "id": "q12",
        "number": 12,
        "type": "radio",
        "required": True,
        "text_en": "When you experience eye discomfort during screen use, what do you usually do?",
        "text_hi": "जब आप स्क्रीन के उपयोग के दौरान आँखों में असुविधा का अनुभव करते हैं, तो आप आमतौर पर क्या करते हैं?",
        "options": [
            {"value": "stop_rest", "text_en": "Stop using the screen and rest my eyes", "text_hi": "स्क्रीन का उपयोग बंद करना और आंखों को आराम देना", "page": 5, "box_idx": 9},
            {"value": "short_break", "text_en": "Take a short break and then resume", "text_hi": "एक छोटा ब्रेक लेना और फिर से शुरू करना", "page": 5, "box_idx": 10},
            {"value": "brightness", "text_en": "Reduce screen brightness / use night mode", "text_hi": "स्क्रीन की ब्राइटनेस कम करना / नाइट मोड का उपयोग करना", "page": 5, "box_idx": 11},
            {"value": "continue", "text_en": "Continue using the screen despite discomfort", "text_hi": "असुविधा के बावजूद स्क्रीन का उपयोग जारी रखना", "page": 5, "box_idx": 12},
            {"value": "rare_discomfort", "text_en": "I rarely experience eye discomfort", "text_hi": "मुझे शायद ही कभी आंखों में असुविधा का अनुभव होता है", "page": 5, "box_idx": 13}
        ]
    },

    # --- SECTION 4 ---
    {
        "id": "q13",
        "number": 13,
        "type": "radio",
        "required": True,
        "text_en": "What is your main reason for using a digital device during the hour before bedtime?",
        "text_hi": "सोने से एक घंटे पहले डिजिटल डिवाइस का उपयोग करने का आपका मुख्य कारण क्या है?",
        "options": [
            {"value": "social", "text_en": "Social media / messaging / chatting", "text_hi": "सोशल मीडिया / मैसेजिंग / चैटिंग", "page": 6, "box_idx": 0},
            {"value": "entertainment", "text_en": "Videos / movies / entertainment", "text_hi": "वीडियो / फिल्में / मनोरंजन", "page": 6, "box_idx": 1},
            {"value": "work", "text_en": "Academic / work-related activities", "text_hi": "शैक्षणिक / कार्य संबंधी गतिविधियां", "page": 6, "box_idx": 2},
            {"value": "gaming", "text_en": "Gaming", "text_hi": "गेमिंग", "page": 6, "box_idx": 3},
            {"value": "reading", "text_en": "Reading / browsing", "text_hi": "पढ़ना / ब्राउज़िंग", "page": 6, "box_idx": 4},
            {"value": "other", "text_en": "Other", "text_hi": "अन्य", "page": 6, "box_idx": 5}
        ]
    },
    {
        "id": "q14",
        "number": 14,
        "type": "radio",
        "required": True,
        "text_en": "How often do you continue using your device after you have decided that you should go to sleep?",
        "text_hi": "यह तय करने के बाद कि आपको सो जाना चाहिए, आप कितनी बार अपने डिवाइस का उपयोग जारी रखते हैं?",
        "options": [
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 6, "box_idx": 6},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 6, "box_idx": 7},
            {"value": "sometimes", "text_en": "Sometimes", "text_hi": "कभी-कभी", "page": 6, "box_idx": 8},
            {"value": "often", "text_en": "Often", "text_hi": "अक्सर", "page": 6, "box_idx": 9},
            {"value": "almost_nightly", "text_en": "Almost every night", "text_hi": "लगभग हर रात", "page": 6, "box_idx": 10}
        ]
    },
    {
        "id": "q15",
        "number": 15,
        "type": "radio",
        "required": True,
        "text_en": "How often do you wake during the night and check your smartphone or another digital device?",
        "text_hi": "आप रात में कितनी बार उठते हैं और अपना स्मार्टफोन या कोई अन्य डिजिटल डिवाइस चेक करते हैं?",
        "options": [
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 6, "box_idx": 11},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 6, "box_idx": 12},
            {"value": "sometimes", "text_en": "Sometimes", "text_hi": "कभी-कभी", "page": 6, "box_idx": 13},
            {"value": "frequently", "text_en": "Frequently", "text_hi": "बार-बार", "page": 6, "box_idx": 14},
            {"value": "almost_nightly", "text_en": "Almost every night", "text_hi": "लगभग हर रात", "page": 6, "box_idx": 15}
        ]
    },
    {
        "id": "q16",
        "number": 16,
        "type": "radio",
        "required": True,
        "text_en": "Where is your primary smartphone kept while you are sleeping?",
        "text_hi": "जब आप सो रहे होते हैं तो आपका मुख्य स्मार्टफोन कहां रखा होता है?",
        "options": [
            {"value": "hand_bed", "text_en": "In my hand / on the bed", "text_hi": "मेरे हाथ में / बिस्तर पर", "page": 7, "box_idx": 0},
            {"value": "beside_bed", "text_en": "Beside my bed", "text_hi": "मेरे बिस्तर के पास", "page": 7, "box_idx": 1},
            {"value": "table_away", "text_en": "On a table/desk away from the bed", "text_hi": "बिस्तर से दूर किसी टेबल/डेस्क पर", "page": 7, "box_idx": 2},
            {"value": "outside_room", "text_en": "Outside the bedroom", "text_hi": "बेडरूम के बाहर", "page": 7, "box_idx": 3},
            {"value": "no_phone", "text_en": "I do not keep a smartphone with me at night", "text_hi": "मैं रात में अपने पास स्मार्टफोन नहीं रखता/रखती", "page": 7, "box_idx": 4}
        ]
    },
    {
        "id": "q17",
        "number": 17,
        "type": "radio",
        "required": True,
        "text_en": "Compared with days when you use less screen time at night, how do you perceive your sleep after prolonged late-night screen use?",
        "text_hi": "रात में कम स्क्रीन समय वाले दिनों की तुलना में, देर रात तक स्क्रीन का उपयोग करने के बाद आप अपनी नींद को कैसा महसूस करते हैं?",
        "options": [
            {"value": "no_diff", "text_en": "No noticeable difference", "text_hi": "कोई उल्लेखनीय अंतर नहीं", "page": 7, "box_idx": 5},
            {"value": "slightly_poorer", "text_en": "Slightly poorer", "text_hi": "थोड़ी खराब", "page": 7, "box_idx": 6},
            {"value": "moderately_poorer", "text_en": "Moderately poorer", "text_hi": "मध्यम रूप से खराब", "page": 7, "box_idx": 7},
            {"value": "much_poorer", "text_en": "Much poorer", "text_hi": "बहुत अधिक खराब", "page": 7, "box_idx": 8},
            {"value": "unsure", "text_en": "I am unsure", "text_hi": "मैं अनिश्चित हूँ", "page": 7, "box_idx": 9}
        ]
    },

    # --- SECTION 5 ---
    {
        "id": "q18",
        "number": 18,
        "type": "radio",
        "required": True,
        "text_en": "How often do smartphone notifications interrupt your studying or work?",
        "text_hi": "स्मार्टफोन नोटिफिकेशन आपकी पढ़ाई या काम में कितनी बार बाधा डालते हैं?",
        "options": [
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 7, "box_idx": 10},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 7, "box_idx": 11},
            {"value": "sometimes", "text_en": "Sometimes", "text_hi": "कभी-कभी", "page": 7, "box_idx": 12},
            {"value": "often", "text_en": "Often", "text_hi": "अक्सर", "page": 7, "box_idx": 13},
            {"value": "very_often", "text_en": "Very often", "text_hi": "बहुत अक्सर", "page": 7, "box_idx": 14}
        ]
    },
    {
        "id": "q19",
        "number": 19,
        "type": "radio",
        "required": True,
        "text_en": "How often does recreational screen use delay the time at which you begin studying or working?",
        "text_hi": "मनोरंजक स्क्रीन उपयोग आपकी पढ़ाई या काम शुरू करने के समय में कितनी बार देरी कराता है?",
        "options": [
            {"value": "never", "text_en": "Never", "text_hi": "कभी नहीं", "page": 8, "box_idx": 0},
            {"value": "rarely", "text_en": "Rarely", "text_hi": "शायद ही कभी", "page": 8, "box_idx": 1},
            {"value": "sometimes", "text_en": "Sometimes", "text_hi": "कभी-कभी", "page": 8, "box_idx": 2},
            {"value": "often", "text_en": "Often", "text_hi": "अक्सर", "page": 8, "box_idx": 3},
            {"value": "almost_daily", "text_en": "Almost every day", "text_hi": "लगभग हर दिन", "page": 8, "box_idx": 4}
        ]
    },
    {
        "id": "q20",
        "number": 20,
        "type": "radio",
        "required": True,
        "text_en": "After a prolonged period of screen use, how difficult do you find it to shift your attention to a non-screen task?",
        "text_hi": "लंबे समय तक स्क्रीन के उपयोग के बाद, अपना ध्यान बिना स्क्रीन वाले कार्य पर केंद्रित करना आपके लिए कितना कठिन होता है?",
        "options": [
            {"value": "not_diff", "text_en": "Not difficult", "text_hi": "कठिन नहीं", "page": 8, "box_idx": 5},
            {"value": "slightly_diff", "text_en": "Slightly difficult", "text_hi": "थोड़ा कठिन", "page": 8, "box_idx": 6},
            {"value": "moderately_diff", "text_en": "Moderately difficult", "text_hi": "मध्यम रूप से कठिन", "page": 8, "box_idx": 7},
            {"value": "very_diff", "text_en": "Very difficult", "text_hi": "बहुत कठिन", "page": 8, "box_idx": 8},
            {"value": "unsure", "text_en": "I am unsure", "text_hi": "मैं अनिश्चित हूँ", "page": 8, "box_idx": 9}
        ]
    },

    # --- SECTION 6 ---
    {
        "id": "q21",
        "number": 21,
        "type": "radio",
        "required": True,
        "text_en": "Before this survey, had you heard of Digital Eye Strain (DES) or Digital Eye Syndrome?",
        "text_hi": "इस सर्वेक्षण से पहले, क्या आपने डिजिटल आई स्ट्रेन (DES) या डिजिटल आई सिंड्रोम के बारे में सुना था?",
        "options": [
            {"value": "understand_well", "text_en": "Yes, and I understand it reasonably well", "text_hi": "हाँ, और मैं इसे काफी अच्छी तरह समझता/समझती हूँ", "page": 8, "box_idx": 10},
            {"value": "little_about", "text_en": "Yes, but I know very little about it", "text_hi": "हाँ, लेकिन मुझे इसके बारे में बहुत कम जानकारी है", "page": 8, "box_idx": 11},
            {"value": "heard_unsure", "text_en": "I have heard the term but am unsure what it means", "text_hi": "मैंने यह शब्द सुना है लेकिन निश्चित नहीं हूँ कि इसका क्या अर्थ है", "page": 8, "box_idx": 12},
            {"value": "never_heard", "text_en": "No, I had never heard of it", "text_hi": "नहीं, मैंने इसके बारे में कभी नहीं सुना था", "page": 8, "box_idx": 13}
        ]
    },
    {
        "id": "q22",
        "number": 22,
        "type": "checkbox",
        "required": False,
        "text_en": "Which measures do you currently use to reduce discomfort during prolonged screen use? Select all that apply.",
        "text_hi": "लंबे समय तक स्क्रीन उपयोग के दौरान असुविधा को कम करने के लिए आप वर्तमान में कौन से उपाय अपनाते हैं? जो लागू हों उन सभी का चयन करें।",
        "options": [
            {"value": "breaks", "text_en": "Taking regular screen breaks", "text_hi": "नियमित रूप से स्क्रीन ब्रेक लेना", "page": 9, "box_idx": 0},
            {"value": "rule_202020", "text_en": "Following the 20-20-20 rule", "text_hi": "20-20-20 नियम का पालन करना", "page": 9, "box_idx": 1},
            {"value": "night_mode", "text_en": "Using night mode / blue-light filter", "text_hi": "नाइट मोड / ब्लू-लाइट फ़िल्टर का उपयोग करना", "page": 9, "box_idx": 2},
            {"value": "brightness", "text_en": "Reducing screen brightness", "text_hi": "स्क्रीन की ब्राइटनेस कम करना", "page": 9, "box_idx": 3},
            {"value": "distance", "text_en": "Increasing viewing distance", "text_hi": "देखने की दूरी बढ़ाना", "page": 9, "box_idx": 4},
            {"value": "posture", "text_en": "Adjusting screen position or posture", "text_hi": "स्क्रीन की स्थिति या पोस्चर (मुद्रा) को समायोजित करना", "page": 9, "box_idx": 5},
            {"value": "none", "text_en": "None of these", "text_hi": "इनमें से कोई नहीं", "page": 9, "box_idx": 6},
            {"value": "other", "text_en": "Other", "text_hi": "अन्य", "page": 9, "box_idx": 7}
        ]
    },
    {
        "id": "q23",
        "number": 23,
        "type": "radio",
        "required": True,
        "text_en": "Which statement best describes your current attitude toward your screen use?",
        "text_hi": "कौन सा कथन आपकी स्क्रीन उपयोग के प्रति आपकी वर्तमान मनोवृत्ति का सबसे अच्छा वर्णन करता है?",
        "options": [
            {"value": "comfortable", "text_en": "I am comfortable with my current screen habits", "text_hi": "मैं अपनी वर्तमान स्क्रीन आदतों से सहज हूँ", "page": 9, "box_idx": 8},
            {"value": "more_no_concern", "text_en": "I use screens more than I would like, but it does not concern me", "text_hi": "मैं जितना चाहता हूँ उससे अधिक स्क्रीन का उपयोग करता हूँ, लेकिन इससे मुझे कोई चिंता नहीं है", "page": 9, "box_idx": 9},
            {"value": "concerned_reduce", "text_en": "I am concerned about my screen use and would like to reduce it", "text_hi": "मैं अपने स्क्रीन उपयोग को लेकर चिंतित हूँ और इसे कम करना चाहूँगा/चाहूँगी", "page": 9, "box_idx": 10},
            {"value": "tried_difficult", "text_en": "I have tried to reduce my screen use but found it difficult", "text_hi": "मैंने अपने स्क्रीन उपयोग को कम करने की कोशिश की है लेकिन यह कठिन लगा", "page": 9, "box_idx": 11},
            {"value": "actively_reduced", "text_en": "I have actively reduced my screen use recently", "text_hi": "मैंने हाल ही में अपने स्क्रीन उपयोग को सक्रिय रूप से कम किया है", "page": 9, "box_idx": 12}
        ]
    }
]

QUESTION_MAP = {q["id"]: q for q in QUESTIONS}

