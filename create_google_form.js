// ============================================================================
// Google Apps Script: Auto-create AcSIR Survey Google Form
// ============================================================================
// HOW TO RUN:
// 1. Open Google Chrome and go to: https://script.google.com/home
// 2. Click "+ New project" (top left).
// 3. Delete everything in the code window, paste ALL of this script.
// 4. Click the "Save" (disk icon) and then click "Run" (play button).
// 5. Google will ask for permission once -> Click "Review permissions" -> Choose your account -> "Advanced" -> "Go to Untitled project (unsafe)" -> "Allow".
// 6. View the Execution Log: It will give you the Form Link and Edit Link instantly!
// ============================================================================

function createAcSIRSurvey() {
  var form = FormApp.create("Screen Use Behaviour, Digital Habits and Visual Well-being (AcSIR-04-SP)");
  
  form.setTitle("Screen Use Behaviour, Digital Habits and Visual Well-being\nस्क्रीन उपयोग व्यवहार, डिजिटल आदतें और दृश्य कल्याण (विज़ुअल वेल-बीइंग)");
  form.setDescription("Societal Program: Problem Understanding and Analysis (AcSIR-04-SP)\n\nInstructions / निर्देश:\nThis survey aims to understand patterns of digital-device use, continuous screen exposure, night-time device use, visual habits, sleep-related behavior, concentration, and strategies used to manage screen exposure.\n\nइस सर्वेक्षण का उद्देश्य डिजिटल डिवाइस के उपयोग के पैटर्न, निरंतर स्क्रीन एक्सपोज़र, रात में डिवाइस के उपयोग, दृश्य आदतों, नींद से संबंधित व्यवहार, एकाग्रता और स्क्रीन एक्सपोज़र को प्रबंधित करने के लिए उपयोग की जाने वाली रणनीतियों को समझना है।");

  // Participant details
  var nameItem = form.addTextItem();
  nameItem.setTitle("Participant Name / प्रतिभागी का पूरा नाम").setRequired(true);
  
  var contactItem = form.addTextItem();
  contactItem.setTitle("Contact / Email / Roll No. (Optional / वैकल्पिक)").setRequired(false);

  // -------------------------------------------------------------
  // SECTION 1 — PARTICIPANT INFORMATION
  // -------------------------------------------------------------
  var pageBreak1 = form.addPageBreakItem();
  pageBreak1.setTitle("SECTION 1 — PARTICIPANT INFORMATION / अनुभाग 1 — प्रतिभागी जानकारी");

  var item1 = form.addMultipleChoiceItem();
  item1.setTitle("Q1. What is your age group?\nआपकी आयु वर्ग क्या है?");
  item1.setChoiceValues(["18–22 years / 18–22 वर्ष", "23–27 years / 23–27 वर्ष", "28–32 years / 28–32 वर्ष", "33 years or above / 33 वर्ष या उससे अधिक", "Prefer not to disclose / ख़ुलासा न करना पसंद करेंगे"]);
  item1.setRequired(true);

  var item2 = form.addMultipleChoiceItem();
  item2.setTitle("Q2. What is your gender?\nआपका लिंग क्या है?");
  item2.setChoiceValues(["Male / पुरुष", "Female / महिला", "Other / अन्य", "Prefer not to disclose / ख़ुलासा न करना पसंद करेंगे"]);
  item2.setRequired(true);

  var item3 = form.addMultipleChoiceItem();
  item3.setTitle("Q3. What is your current living arrangement?\nआपकी वर्तमान रहने की व्यवस्था क्या है?");
  item3.setChoiceValues(["Living alone / अकेले रहना", "Living with parents/family / माता-पिता/परिवार के साथ रहना", "Living with spouse/partner / जीवनसाथी/पार्टनर के साथ रहना", "Living with roommates/peers / रूममेट्स/साथियों के साथ रहना", "Hostel/residential accommodation / हॉस्टल/आवासीय आवास", "Other / अन्य"]);
  item3.setRequired(true);

  // -------------------------------------------------------------
  // SECTION 2 — DAILY SCREEN-USE PATTERN
  // -------------------------------------------------------------
  var pageBreak2 = form.addPageBreakItem();
  pageBreak2.setTitle("SECTION 2 — DAILY SCREEN-USE PATTERN / अनुभाग 2 — दैनिक स्क्रीन-उपयोग पैटर्न");

  var item4 = form.addMultipleChoiceItem();
  item4.setTitle("Q4. On a typical day, approximately how many total hours do you spend using digital screens for all purposes?\nएक सामान्य दिन में, आप सभी उद्देश्यों के लिए डिजिटल स्क्रीन का उपयोग करने में कुल कितने घंटे बिताते हैं?");
  item4.setChoiceValues(["Less than 3 hours / 3 घंटे से कम", "3–5 hours / 3–5 घंटे", "5–7 hours / 5–7 घंटे", "7–9 hours / 7–9 घंटे", "10 hours or more / 10 घंटे या उससे अधिक"]);
  item4.setRequired(true);

  var item5 = form.addMultipleChoiceItem();
  item5.setTitle("Q5. During a typical weekday, during which period do you spend the most time using digital screens?\nएक सामान्य कार्यदिवस के दौरान, आप किस अवधि में डिजिटल स्क्रीन का उपयोग करने में सबसे अधिक समय बिताते हैं?");
  item5.setChoiceValues(["Morning (6 AM–12 PM) / सुबह (सुबह 6 बजे से दोपहर 12 बजे तक)", "Afternoon (12 PM–5 PM) / दोपहर (दोपहर 12 बजे से शाम 5 बजे तक)", "Evening (5 PM–9 PM) / शाम (शाम 5 बजे से रात 9 बजे तक)", "Late night (after 9 PM) / देर रात (रात 9 बजे के बाद)", "Screen use is fairly evenly distributed throughout the day / स्क्रीन का उपयोग पूरे दिन समान रूप से वितरित रहता है"]);
  item5.setRequired(true);

  var item6 = form.addMultipleChoiceItem();
  item6.setTitle("Q6. What is your most common reason for using a digital screen for non-academic/non-work purposes?\nगैर-शैक्षणिक/गैर-कार्य उद्देश्यों के लिए डिजिटल स्क्रीन का उपयोग करने का आपका सबसे सामान्य कारण क्या है?");
  item6.setChoiceValues(["social media / messaging / chatting / सोशल मीडिया / मैसेजिंग / चैटिंग", "Watching videos / movies / streaming / वीडियो / फिल्में देखना / स्ट्रीमिंग", "Online gaming / ऑनलाइन गेमिंग", "Browsing / news / general internet use / ब्राउज़िंग / समाचार / सामान्य इंटरनेट उपयोग", "Online shopping / ऑनलाइन शॉपिंग", "Other / अन्य"]);
  item6.setRequired(true);

  // -------------------------------------------------------------
  // SECTION 3 — CONTINUOUS SCREEN EXPOSURE AND VISUAL HABITS
  // -------------------------------------------------------------
  var pageBreak3 = form.addPageBreakItem();
  pageBreak3.setTitle("SECTION 3 — CONTINUOUS SCREEN EXPOSURE AND VISUAL HABITS / अनुभाग 3 — निरंतर स्क्रीन एक्सपोज़र और दृश्य आदतें");

  var item7 = form.addMultipleChoiceItem();
  item7.setTitle("Q7. How often do you check your smartphone when you do not have a specific task or notification requiring you to do so?\nजब आपके पास ऐसा करने के लिए कोई विशिष्ट कार्य या सूचना (नोटिफिकेशन) नहीं होती है, तब आप कितनी बार अपना स्मार्टफोन चेक करते हैं?");
  item7.setChoiceValues(["Rarely or never / शायद ही कभी या कभी नहीं", "Occasionally / कभी-कभार", "Several times a day / दिन में कई बार", "Frequently throughout the day / पूरे दिन बार-बार", "Almost continuously / लगभग लगातार"]);
  item7.setRequired(true);

  var item8 = form.addMultipleChoiceItem();
  item8.setTitle("Q8. How often does your recreational screen use continue longer than you originally intended?\nआपका मनोरंजक स्क्रीन उपयोग आपकी मूल मंशा से अधिक समय तक कितनी बार जारी रहता है?");
  item8.setChoiceValues(["Never / कभी नहीं", "Rarely / शायद ही कभी", "Sometimes / कभी-कभी", "Often / अक्सर", "Almost always / लगभग हमेशा"]);
  item8.setRequired(true);

  var item9 = form.addMultipleChoiceItem();
  item9.setTitle("Q9. What is the longest period you usually spend continuously looking at a screen without taking a meaningful break?\nबिना कोई सार्थक ब्रेक लिए आप आमतौर पर स्क्रीन को लगातार देखने में सबसे लंबा कितना समय बिताते हैं?");
  item9.setChoiceValues(["Less than 30 minutes / 30 मिनट से कम", "30–60 minutes / 30–60 मिनट", "1–2 hours / 1–2 घंटे", "2–3 hours / 2–3 घंटे", "More than 3 hours / 3 घंटे से अधिक"]);
  item9.setRequired(true);

  var item10 = form.addMultipleChoiceItem();
  item10.setTitle("Q10. How often do you use a digital screen in a dark or poorly lit environment?\nआप अँधेरे या कम रोशनी वाले वातावरण में डिजिटल स्क्रीन का उपयोग कितनी बार करते हैं?");
  item10.setChoiceValues(["Never / कभी नहीं", "Rarely / शायद ही कभी", "Sometimes / कभी-कभी", "Often / अक्सर", "Almost every day / लगभग हर दिन"]);
  item10.setRequired(true);

  var item11 = form.addMultipleChoiceItem();
  item11.setTitle("Q11. How often do you deliberately look away from the screen or take a visual break during prolonged screen use?\nलंबे समय तक स्क्रीन के उपयोग के दौरान आप कितनी बार जानबूझकर स्क्रीन से दूर देखते हैं या आँखों को आराम देने के लिए ब्रेक लेते हैं?");
  item11.setChoiceValues(["Every 20–30 minutes / हर 20–30 मिनट में", "Every 30–60 minutes / हर 30–60 मिनट में", "Only after completing a task / कार्य पूरा करने के बाद ही", "Rarely / शायद ही कभी", "Never / कभी नहीं"]);
  item11.setRequired(true);

  var item12 = form.addMultipleChoiceItem();
  item12.setTitle("Q12. When you experience eye discomfort during screen use, what do you usually do?\nजब आप स्क्रीन के उपयोग के दौरान आँखों में असुविधा का अनुभव करते हैं, तो आप आमतौर पर क्या करते हैं?");
  item12.setChoiceValues(["Stop using the screen and rest my eyes / स्क्रीन का उपयोग बंद करना और आंखों को आराम देना", "Take a short break and then resume / एक छोटा ब्रेक लेना और फिर से शुरू करना", "Reduce screen brightness / use night mode / स्क्रीन की ब्राइटनेस कम करना / नाइट मोड का उपयोग करना", "Continue using the screen despite discomfort / असुविधा के बावजूद स्क्रीन का उपयोग जारी रखना", "I rarely experience eye discomfort / मुझे शायद ही कभी आंखों में असुविधा का अनुभव होता है"]);
  item12.setRequired(true);

  // -------------------------------------------------------------
  // SECTION 4 — NIGHT-TIME DIGITAL BEHAVIOUR
  // -------------------------------------------------------------
  var pageBreak4 = form.addPageBreakItem();
  pageBreak4.setTitle("SECTION 4 — NIGHT-TIME DIGITAL BEHAVIOUR / अनुभाग 4 — रात के समय डिजिटल व्यवहार");

  var item13 = form.addMultipleChoiceItem();
  item13.setTitle("Q13. What is your main reason for using a digital device during the hour before bedtime?\nसोने से एक घंटे पहले डिजिटल डिवाइस का उपयोग करने का आपका मुख्य कारण क्या है?");
  item13.setChoiceValues(["Social media / messaging / chatting / सोशल मीडिया / मैसेजिंग / चैटिंग", "Videos / movies / entertainment / वीडियो / फिल्में / मनोरंजन", "Academic / work-related activities / शैक्षणिक / कार्य संबंधी गतिविधियां", "Gaming / गेमिंग", "Reading / browsing / पढ़ना / ब्राउज़िंग", "Other / अन्य"]);
  item13.setRequired(true);

  var item14 = form.addMultipleChoiceItem();
  item14.setTitle("Q14. How often do you continue using your device after you have decided that you should go to sleep?\nयह तय करने के बाद कि आपको सो जाना चाहिए, आप कितनी बार अपने डिवाइस का उपयोग जारी रखते हैं?");
  item14.setChoiceValues(["Never / कभी नहीं", "Rarely / शायद ही कभी", "Sometimes / कभी-कभी", "Often / अक्सर", "Almost every night / लगभग हर रात"]);
  item14.setRequired(true);

  var item15 = form.addMultipleChoiceItem();
  item15.setTitle("Q15. How often do you wake during the night and check your smartphone or another digital device?\nआप रात में कितनी बार उठते हैं और अपना स्मार्टफोन या कोई अन्य डिजिटल डिवाइस चेक करते हैं?");
  item15.setChoiceValues(["Never / कभी नहीं", "Rarely / शायद ही कभी", "Sometimes / कभी-कभी", "Frequently / बार-बार", "Almost every night / लगभग हर रात"]);
  item15.setRequired(true);

  var item16 = form.addMultipleChoiceItem();
  item16.setTitle("Q16. Where is your primary smartphone kept while you are sleeping?\nजब आप सो रहे होते हैं तो आपका मुख्य स्मार्टफोन कहां रखा होता है?");
  item16.setChoiceValues(["In my hand / on the bed / मेरे हाथ में / बिस्तर पर", "Beside my bed / मेरे बिस्तर के पास", "On a table/desk away from the bed / बिस्तर से दूर किसी टेबल/डेस्क पर", "Outside the bedroom / बेडरूम के बाहर", "I do not keep a smartphone with me at night / मैं रात में अपने पास स्मार्टफोन नहीं रखता/रखती"]);
  item16.setRequired(true);

  var item17 = form.addMultipleChoiceItem();
  item17.setTitle("Q17. Compared with days when you use less screen time at night, how do you perceive your sleep after prolonged late-night screen use?\nरात में कम स्क्रीन समय वाले दिनों की तुलना में, देर रात तक स्क्रीन का उपयोग करने के बाद आप अपनी नींद को कैसा महसूस करते हैं?");
  item17.setChoiceValues(["No noticeable difference / कोई उल्लेखनीय अंतर नहीं", "Slightly poorer / थोड़ी खराब", "Moderately poorer / मध्यम रूप से खराब", "Much poorer / बहुत अधिक खराब", "I am unsure / मैं अनिश्चित हूँ"]);
  item17.setRequired(true);

  // -------------------------------------------------------------
  // SECTION 5 — CONCENTRATION AND DAILY FUNCTIONING
  // -------------------------------------------------------------
  var pageBreak5 = form.addPageBreakItem();
  pageBreak5.setTitle("SECTION 5 — CONCENTRATION AND DAILY FUNCTIONING / अनुभाग 5 — एकाग्रता और दैनिक कार्यप्रणाली");

  var item18 = form.addMultipleChoiceItem();
  item18.setTitle("Q18. How often do smartphone notifications interrupt your studying or work?\nस्मार्टफोन नोटिफिकेशन आपकी पढ़ाई या काम में कितनी बार बाधा डालते हैं?");
  item18.setChoiceValues(["Never / कभी नहीं", "Rarely / शायद ही कभी", "Sometimes / कभी-कभी", "Often / अक्सर", "Very often / बहुत अक्सर"]);
  item18.setRequired(true);

  var item19 = form.addMultipleChoiceItem();
  item19.setTitle("Q19. How often does recreational screen use delay the time at which you begin studying or working?\nमनोरंजक स्क्रीन उपयोग आपकी पढ़ाई या काम शुरू करने के समय में कितनी बार देरी कराता है?");
  item19.setChoiceValues(["Never / कभी नहीं", "Rarely / शायद ही कभी", "Sometimes / कभी-कभी", "Often / अक्सर", "Almost every day / लगभग हर दिन"]);
  item19.setRequired(true);

  var item20 = form.addMultipleChoiceItem();
  item20.setTitle("Q20. After a prolonged period of screen use, how difficult do you find it to shift your attention to a non-screen task?\nलंबे समय तक स्क्रीन के उपयोग के बाद, अपना ध्यान बिना स्क्रीन वाले कार्य पर केंद्रित करना आपके लिए कितना कठिन होता है?");
  item20.setChoiceValues(["Not difficult / कठिन नहीं", "Slightly difficult / थोड़ा कठिन", "Moderately difficult / मध्यम रूप से कठिन", "Very difficult / बहुत कठिन", "I am unsure / मैं अनिश्चित हूँ"]);
  item20.setRequired(true);

  // -------------------------------------------------------------
  // SECTION 6 — AWARENESS AND PREVENTIVE PRACTICES
  // -------------------------------------------------------------
  var pageBreak6 = form.addPageBreakItem();
  pageBreak6.setTitle("SECTION 6 — AWARENESS AND PREVENTIVE PRACTICES / अनुभाग 6 — जागरूकता और निवारक उपाय");

  var item21 = form.addMultipleChoiceItem();
  item21.setTitle("Q21. Before this survey, had you heard of Digital Eye Strain (DES) or Digital Eye Syndrome?\nइस सर्वेक्षण से पहले, क्या आपने डिजिटल आई स्ट्रेन (DES) या डिजिटल आई सिंड्रोम के बारे में सुना था?");
  item21.setChoiceValues(["Yes, and I understand it reasonably well / हाँ, और मैं इसे काफी अच्छी तरह समझता/समझती हूँ", "Yes, but I know very little about it / हाँ, लेकिन मुझे इसके बारे में बहुत कम जानकारी है", "I have heard the term but am unsure what it means / मैंने यह शब्द सुना है लेकिन निश्चित नहीं हूँ कि इसका क्या अर्थ है", "No, I had never heard of it / नहीं, मैंने इसके बारे में कभी नहीं सुना था"]);
  item21.setRequired(true);

  var item22 = form.addCheckboxItem();
  item22.setTitle("Q22. Which measures do you currently use to reduce discomfort during prolonged screen use? Select all that apply.\nलंबे समय तक स्क्रीन उपयोग के दौरान असुविधा को कम करने के लिए आप वर्तमान में कौन से उपाय अपनाते हैं? जो लागू हों उन सभी का चयन करें।");
  item22.setChoiceValues(["Taking regular screen breaks / नियमित रूप से स्क्रीन ब्रेक लेना", "Following the 20-20-20 rule / 20-20-20 नियम का पालन करना", "Using night mode / blue-light filter / नाइट मोड / ब्लू-लाइट फ़िल्टर का उपयोग करना", "Reducing screen brightness / स्क्रीन की ब्राइटनेस कम करना", "Increasing viewing distance / देखने की दूरी बढ़ाना", "Adjusting screen position or posture / स्क्रीन की स्थिति या पोस्चर (मुद्रा) को समायोजित करना", "None of these / इनमें से कोई नहीं", "Other / अन्य"]);
  item22.setRequired(false);

  var item23 = form.addMultipleChoiceItem();
  item23.setTitle("Q23. Which statement best describes your current attitude toward your screen use?\nकौन सा कथन आपकी स्क्रीन उपयोग के प्रति आपकी वर्तमान मनोवृत्ति का सबसे अच्छा वर्णन करता है?");
  item23.setChoiceValues(["I am comfortable with my current screen habits / मैं अपनी वर्तमान स्क्रीन आदतों से सहज हूँ", "I use screens more than I would like, but it does not concern me / मैं जितना चाहता हूँ उससे अधिक स्क्रीन का उपयोग करता हूँ, लेकिन इससे मुझे कोई चिंता नहीं है", "I am concerned about my screen use and would like to reduce it / मैं अपने स्क्रीन उपयोग को लेकर चिंतित हूँ और इसे कम करना चाहूँगा/चाहूँगी", "I have tried to reduce my screen use but found it difficult / मैंने अपने स्क्रीन उपयोग को कम करने की कोशिश की है लेकिन यह कठिन लगा", "I have actively reduced my screen use recently / मैंने हाल ही में अपने स्क्रीन उपयोग को सक्रिय रूप से कम किया है"]);
  item23.setRequired(true);

  Logger.log("=================================================");
  Logger.log("FORM CREATED SUCCESSFULLY!");
  Logger.log("1. Edit Form URL: " + form.getEditUrl());
  Logger.log("2. Share Link for Respondents: " + form.getPublishedUrl());
  Logger.log("=================================================");
}
