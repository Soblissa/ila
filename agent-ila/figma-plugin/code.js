// ILA Agent Screen Builder — Figma Plugin
// Version 2.0 — mit Komponenten-Index, kein loadAllPagesAsync
"use strict";

const FRAME_SIZES = {
  desktop: { width: 1440, height: 900 },
  mobile: { width: 390, height: 844 },
};

// Komponenten-Index — wird vom Plugin geladen
let COMPONENT_INDEX = null;

async function loadComponentIndex() {
  if (COMPONENT_INDEX) return COMPONENT_INDEX;
  // Index ist in den Plugin-Daten eingebettet
  COMPONENT_INDEX = {"Navigation Bar Main": {"nodeId": "58:24478", "originalName": "Navigation Bar Main 🆕", "width": 64, "height": 1034, "foundIn": "ila-L/Start"}, "Logo iLa": {"nodeId": "I58:24516;7902:11921", "originalName": "Logo iLa", "width": 35, "height": 28, "foundIn": "ila-L/Start emptystate"}, "_Navigation Item Top-Level": {"nodeId": "I58:24478;7902:11879", "originalName": "_Navigation Item Top-Level", "width": 48, "height": 48, "foundIn": "ila-L/Start"}, "Icon": {"nodeId": "I155:16993;4096:948", "originalName": "Icon", "width": 24, "height": 24, "foundIn": "ila-L/Frderungen"}, "Support": {"nodeId": "I58:24478;7902:11880", "originalName": "Support", "width": 48, "height": 48, "foundIn": "ila-L/Start"}, "FAQ": {"nodeId": "I58:24478;7902:11881", "originalName": "FAQ", "width": 48, "height": 48, "foundIn": "ila-L/Start"}, "Favorites": {"nodeId": "I58:24478;7902:11883", "originalName": "Favorites", "width": 48, "height": 48, "foundIn": "ila-L/Start"}, "Open/Close": {"nodeId": "I58:24478;7903:12117", "originalName": "Open/Close", "width": 48, "height": 48, "foundIn": "ila-L/Start"}, "Navigation Bar Content": {"nodeId": "58:24480", "originalName": "Navigation Bar Content", "width": 1216, "height": 64, "foundIn": "ila-L/Start"}, "_Profile": {"nodeId": "I58:24516;7902:11924", "originalName": "_Profile", "width": 48, "height": 48, "foundIn": "ila-L/Start emptystate"}, "Button Icon": {"nodeId": "I5:43896;7342:10324", "originalName": "Button Icon", "width": 48, "height": 48, "foundIn": "iF-L/Frderplan/Frderziele hinzufgen"}, "Heading Widget": {"nodeId": "58:24487", "originalName": "Heading Widget", "width": 683, "height": 20, "foundIn": "ila-L/Start"}, "Link": {"nodeId": "I58:24487;6349:4382", "originalName": "Link", "width": 95, "height": 20, "foundIn": "ila-L/Start"}, "List-Item Widget Timestamp": {"nodeId": "58:24489", "originalName": "List-Item Widget Timestamp", "width": 683, "height": 74, "foundIn": "ila-L/Start"}, "Content": {"nodeId": "I58:24489;6351:4420", "originalName": "Content", "width": 521, "height": 42, "foundIn": "ila-L/Start"}, "Timestamp": {"nodeId": "I58:24489;6351:4421", "originalName": "Timestamp", "width": 74, "height": 20, "foundIn": "ila-L/Start"}, "chevron-right": {"nodeId": "I58:24489;6351:4422", "originalName": "chevron-right", "width": 24, "height": 24, "foundIn": "ila-L/Start"}, "Stats": {"nodeId": "58:24496", "originalName": "Stats", "width": 277, "height": 90, "foundIn": "ila-L/Start"}, "Button": {"nodeId": "4:58320", "originalName": "Button", "width": 122, "height": 48, "foundIn": "ila-L/Frderziel in Planung"}, "Title Section Action": {"nodeId": "58:24503", "originalName": "Title Section Action", "width": 954, "height": 33, "foundIn": "ila-L/Start"}, "Action": {"nodeId": "I485:13051;6587:19059", "originalName": "Action", "width": 104, "height": 48, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "Badge": {"nodeId": "I485:13051;6587:19059;6860:24252", "originalName": "Badge", "width": 24, "height": 24, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "Accordion Header": {"nodeId": "58:24506", "originalName": "Accordion Header", "width": 922, "height": 60, "foundIn": "ila-L/Start"}, "Menu": {"nodeId": "I58:24516;7902:11919", "originalName": "Menu", "width": 48, "height": 48, "foundIn": "ila-L/Start emptystate"}, "Button Icon Inverted": {"nodeId": "I58:24516;7902:11924;7503:7377", "originalName": "Button Icon Inverted", "width": 48, "height": 48, "foundIn": "ila-L/Start emptystate"}, "Accordion Panel Text": {"nodeId": "59:6695", "originalName": "Accordion Panel Text", "width": 922, "height": 248, "foundIn": "ila-L/Start/Full Content"}, "Title": {"nodeId": "155:16980", "originalName": "Title", "width": 832, "height": 40, "foundIn": "ila-L/Frderungen"}, "Input Search": {"nodeId": "155:16984", "originalName": "Input Search", "width": 832, "height": 56, "foundIn": "ila-L/Frderungen"}, "search": {"nodeId": "I155:16984;4100:1507", "originalName": "search", "width": 24, "height": 24, "foundIn": "ila-L/Frderungen"}, "Heading List": {"nodeId": "155:16986", "originalName": "Heading List", "width": 800, "height": 20, "foundIn": "ila-L/Frderungen"}, "List-Item Support": {"nodeId": "155:16988", "originalName": "List-Item Support", "width": 800, "height": 74, "foundIn": "ila-L/Frderungen"}, "_Tag Group": {"nodeId": "I155:16988;5322:1985", "originalName": "_Tag Group", "width": 210, "height": 32, "foundIn": "ila-L/Frderungen"}, "Button Floating": {"nodeId": "155:16993", "originalName": "Button Floating", "width": 234, "height": 56, "foundIn": "ila-L/Frderungen"}, "macOS bar": {"nodeId": "157:23526", "originalName": "macOS bar", "width": 1280, "height": 85, "foundIn": "ila-L/FAQ Overview"}, "Menu Bar": {"nodeId": "I157:23526;4584:12661", "originalName": "Menu Bar", "width": 1280, "height": 32, "foundIn": "ila-L/FAQ Overview"}, "Apple Logo": {"nodeId": "I157:23526;4584:12661;121:13231", "originalName": "Apple Logo", "width": 37, "height": 24, "foundIn": "ila-L/FAQ Overview"}, "App Name": {"nodeId": "I157:23526;4584:12661;121:13232", "originalName": "App Name", "width": 90, "height": 24, "foundIn": "ila-L/FAQ Overview"}, "Menu Item - Leading": {"nodeId": "I157:23526;4584:12661;121:13233", "originalName": "Menu Item - Leading", "width": 51, "height": 24, "foundIn": "ila-L/FAQ Overview"}, "Menu Item - Trailing": {"nodeId": "I157:23526;4584:12661;121:13225", "originalName": "Menu Item - Trailing", "width": 40, "height": 24, "foundIn": "ila-L/FAQ Overview"}, "Safari (Big Sur) / Toolbar / Dark": {"nodeId": "I157:23526;4584:12662", "originalName": "Safari (Big Sur) / Toolbar / Dark", "width": 1280, "height": 53, "foundIn": "ila-L/FAQ Overview"}, "Safari (Big Sur) / Toolbar / Light": {"nodeId": "I157:23526;4584:12662;2033:88", "originalName": "Safari (Big Sur) / Toolbar / Light", "width": 1280, "height": 53, "foundIn": "ila-L/FAQ Overview"}, "Traffic Lights (Big Sur)": {"nodeId": "I157:23526;4584:12662;2033:88;2033:80", "originalName": "Traffic Lights (Big Sur)", "width": 52, "height": 12, "foundIn": "ila-L/FAQ Overview"}, "Safari (Big Sur) / Search Bar (Default)": {"nodeId": "I157:23526;4584:12662;2033:88;2033:84", "originalName": "Safari (Big Sur) / Search Bar (Default)", "width": 516, "height": 28, "foundIn": "ila-L/FAQ Overview"}, "Title Page": {"nodeId": "157:23531", "originalName": "Title Page", "width": 954, "height": 40, "foundIn": "ila-L/FAQ Overview"}, "Title Section": {"nodeId": "157:23534", "originalName": "Title Section", "width": 954, "height": 33, "foundIn": "ila-L/FAQ Overview"}, "_Top-Level Navigation Item": {"nodeId": "I1:3394;7902:11879", "originalName": "_Top-Level Navigation Item", "width": 48, "height": 48, "foundIn": "ila-L/Frderakte"}, "Header Page Support": {"nodeId": "1:3398", "originalName": "Header Page Support", "width": 832, "height": 136, "foundIn": "ila-L/Frderakte"}, "Accordion Header Support": {"nodeId": "1:3403", "originalName": "Accordion Header Support", "width": 832, "height": 104, "foundIn": "ila-L/Frderakte"}, "Notification": {"nodeId": "5:43562", "originalName": "Notification", "width": 960, "height": 88, "foundIn": "iF-L/Frderplan/Initial"}, "Print": {"nodeId": "1:3773", "originalName": "Print", "width": 96, "height": 36, "foundIn": "ila-L/Frderakte"}, "More": {"nodeId": "1:3775", "originalName": "More", "width": 32, "height": 32, "foundIn": "ila-L/Frderakte"}, "more-vertical": {"nodeId": "I1:3775;4260:1103", "originalName": "more-vertical", "width": 16, "height": 16, "foundIn": "ila-L/Frderakte"}, "Tag": {"nodeId": "I4:59423;7834:1725", "originalName": "Tag", "width": 152, "height": 32, "foundIn": "ila-L/Frderziel in Durchfhrung evaluiert"}, "Tag Number": {"nodeId": "5:44241", "originalName": "Tag Number", "width": 194, "height": 32, "foundIn": "iF-L/Frderplan/Updates"}, "Card Target": {"nodeId": "967:107299", "originalName": "Card Target", "width": 336, "height": 261, "foundIn": "ila-L/Frderakte/DragDrop Frderziel 2"}, "Status Evaluation": {"nodeId": "I967:107299;8280:1306", "originalName": "Status Evaluation", "width": 113, "height": 20, "foundIn": "ila-L/Frderakte/DragDrop Frderziel 2"}, "Accordion Tasks": {"nodeId": "I967:107299;7979:8076", "originalName": "Accordion Tasks", "width": 336, "height": 149, "foundIn": "ila-L/Frderakte/DragDrop Frderziel 2"}, "Heading": {"nodeId": "I967:107299;7979:8076;7995:6790", "originalName": "Heading", "width": 336, "height": 36, "foundIn": "ila-L/Frderakte/DragDrop Frderziel 2"}, "Panel": {"nodeId": "I967:107299;7979:8076;7995:6791", "originalName": "Panel", "width": 336, "height": 113, "foundIn": "ila-L/Frderakte/DragDrop Frderziel 2"}, "Cursors / Pointer": {"nodeId": "967:107246", "originalName": "Cursors / Pointer", "width": 24, "height": 24, "foundIn": "ila-L/Frderakte/DragDrop Frderziel 2"}, "Page Heading Plan": {"nodeId": "5:44769", "originalName": "Page Heading Plan", "width": 1024, "height": 104, "foundIn": "iF-L/Frderplan/PDF"}, "Close": {"nodeId": "I5:44706;7073:20162", "originalName": "Close", "width": 32, "height": 32, "foundIn": "iF-L/Frderplan/Updated"}, "_Text Input": {"nodeId": "5:43567", "originalName": "_Text Input", "width": 960, "height": 48, "foundIn": "iF-L/Frderplan/Initial"}, "Input Multiline": {"nodeId": "I5:43567;14542:89567", "originalName": "Input Multiline", "width": 960, "height": 48, "foundIn": "iF-L/Frderplan/Initial"}, "trash-2": {"nodeId": "I4:58320;4099:636", "originalName": "trash-2", "width": 20, "height": 20, "foundIn": "ila-L/Frderziel in Planung"}, "share": {"nodeId": "I5:43578;4524:3252", "originalName": "share", "width": 20, "height": 20, "foundIn": "iF-L/Frderplan/Initial"}, "download": {"nodeId": "I5:43579;4524:3252", "originalName": "download", "width": 20, "height": 20, "foundIn": "iF-L/Frderplan/Initial"}, "Snackbar": {"nodeId": "5:43677", "originalName": "Snackbar", "width": 362, "height": 48, "foundIn": "iF-L/Frderplan/Strken/Gespeichert"}, "Input Text Multiline": {"nodeId": "5:43748", "originalName": "Input Text Multiline", "width": 960, "height": 72, "foundIn": "iF-L/Frderplan/Strken//Texteingabe"}, "Focus": {"nodeId": "I5:43748;7937:127525", "originalName": "Focus", "width": 960, "height": 72, "foundIn": "iF-L/Frderplan/Strken//Texteingabe"}, "Modal Page": {"nodeId": "5:43896", "originalName": "Modal Page", "width": 1280, "height": 1090, "foundIn": "iF-L/Frderplan/Frderziele hinzufgen"}, "Modal/Frderziele hinzufgen": {"nodeId": "I5:43896;7342:10317", "originalName": "Modal/Förderziele hinzufügen", "width": 1024, "height": 974, "foundIn": "iF-L/Frderplan/Frderziele hinzufgen"}, "Card Target Select": {"nodeId": "I5:43896;7342:10317;5:45199", "originalName": "Card Target Select", "width": 331, "height": 184, "foundIn": "iF-L/Frderplan/Frderziele hinzufgen"}, "Spacer": {"nodeId": "I5:43896;7342:10317;5:45203", "originalName": "Spacer", "width": 331, "height": 184, "foundIn": "iF-L/Frderplan/Frderziele hinzufgen"}, "Scrollbar Vertical": {"nodeId": "I5:43896;7342:10319", "originalName": "Scrollbar Vertical", "width": 4, "height": 744, "foundIn": "iF-L/Frderplan/Frderziele hinzufgen"}, "Target List Item In Progress": {"nodeId": "5:44795", "originalName": "Target List Item In Progress", "width": 1024, "height": 653, "foundIn": "iF-L/Frderplan/PDF"}, "Target List Item Planned": {"nodeId": "5:44796", "originalName": "Target List Item Planned", "width": 1024, "height": 253, "foundIn": "iF-L/Frderplan/PDF"}, "Header Page Target": {"nodeId": "4:58304", "originalName": "Header Page Target", "width": 1088, "height": 196, "foundIn": "ila-L/Frderziel in Planung"}, "Status": {"nodeId": "I4:58304;6870:22429", "originalName": "Status", "width": 92, "height": 32, "foundIn": "ila-L/Frderziel in Planung"}, "Evaluation": {"nodeId": "I4:58304;7834:1725", "originalName": "Evaluation", "width": 66, "height": 32, "foundIn": "ila-L/Frderziel in Planung"}, "Bereich": {"nodeId": "I4:58304;6870:22430", "originalName": "Bereich", "width": 81, "height": 32, "foundIn": "ila-L/Frderziel in Planung"}, "book-open": {"nodeId": "I4:58304;6870:22430;5427:21083", "originalName": "book-open", "width": 16, "height": 16, "foundIn": "ila-L/Frderziel in Planung"}, "Klasse": {"nodeId": "I4:58304;6870:22431", "originalName": "Klasse", "width": 74, "height": 32, "foundIn": "ila-L/Frderziel in Planung"}, "Responsability": {"nodeId": "I4:58304;7921:7967", "originalName": "Responsability", "width": 188, "height": 20, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Item Kurs": {"nodeId": "4:58311", "originalName": "Accordion-Item Kurs", "width": 1056, "height": 112, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion Header Task": {"nodeId": "I4:58311;4:57338", "originalName": "Accordion Header Task", "width": 1056, "height": 112, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Item Vorschlag": {"nodeId": "4:58312", "originalName": "Accordion-Item Vorschlag", "width": 1056, "height": 136, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Item Eigene Manahme": {"nodeId": "4:58315", "originalName": "Accordion-Item Eigene Maßnahme", "width": 1056, "height": 112, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Item Hinzufgen": {"nodeId": "4:58316", "originalName": "Accordion-Item Hinzufügen", "width": 1056, "height": 80, "foundIn": "ila-L/Frderziel in Planung"}, "List-Item Add": {"nodeId": "I4:58316;4:57354", "originalName": "List-Item Add", "width": 1056, "height": 80, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Panel Vorschlag": {"nodeId": "I4:58405;4:58237", "originalName": "Accordion-Panel Vorschlag", "width": 1056, "height": 192, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Panel Notiz": {"nodeId": "I4:58657;4:58277", "originalName": "Accordion-Panel Notiz", "width": 800, "height": 164, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Item Vorschlag/Planning/Default/True/False": {"nodeId": "4:58879", "originalName": "Accordion-Item Vorschlag/Planning/Default/True/False", "width": 1056, "height": 144, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion Action 14": {"nodeId": "I4:58879;18635:184175", "originalName": "Accordion Action 14", "width": 1056, "height": 144, "foundIn": "ila-L/Frderziel in Planung"}, "Accordion-Panel Eigene Manahme": {"nodeId": "I4:58904;4:57251", "originalName": "Accordion-Panel Eigene Maßnahme", "width": 1056, "height": 248, "foundIn": "ila-L/Frderziel in Planung"}, "loader": {"nodeId": "I4:59423;7834:1725;7073:20216", "originalName": "loader", "width": 16, "height": 16, "foundIn": "ila-L/Frderziel in Durchfhrung evaluiert"}, "_Specs responsability": {"nodeId": "I875:42594;7921:7967", "originalName": "_Specs responsability", "width": 164, "height": 20, "foundIn": "ila-L/Frderziel in Durchfhrung evaluiert"}, "Teaser": {"nodeId": "29:46005", "originalName": "Teaser", "width": 1088, "height": 160, "foundIn": "ila-L/Start/Teaser Fragebogen"}, "Modal Alert": {"nodeId": "53:68099", "originalName": "Modal Alert", "width": 1280, "height": 832, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "Slot/User Feedback v2": {"nodeId": "I53:68099;4608:4930", "originalName": "Slot/User Feedback v2", "width": 432, "height": 406, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "_Rating": {"nodeId": "I53:68099;4608:4930;53:69933", "originalName": "_Rating", "width": 312, "height": 80, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "_Feedback Item": {"nodeId": "I53:68099;4608:4930;53:69933;53:70105", "originalName": "_Feedback Item", "width": 56, "height": 56, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "_Input": {"nodeId": "I53:68099;4608:4930;53:69934", "originalName": "_Input", "width": 432, "height": 120, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "Checkbox": {"nodeId": "I53:68099;4608:4930;53:69934;53:70080", "originalName": "Checkbox", "width": 432, "height": 40, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "Input Checkbox": {"nodeId": "I53:68099;4608:4930;53:69934;53:70080;53:70035", "originalName": "Input Checkbox", "width": 20, "height": 20, "foundIn": "iF-L/Schlerdetailseite/Feedback"}, "Modal Wizard": {"nodeId": "485:13051", "originalName": "Modal Wizard", "width": 1280, "height": 900, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "Header": {"nodeId": "I485:13051;7227:23332", "originalName": "Header", "width": 560, "height": 64, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "_Progress Bar": {"nodeId": "I485:13051;7227:23332;8198:4942", "originalName": "_Progress Bar", "width": 560, "height": 4, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "_Wizard/Neue Frderung/Schritt 1: Schlersuche": {"nodeId": "I485:13051;4608:5046", "originalName": "_Wizard/Neue Förderung/Schritt 1: Schülersuche", "width": 432, "height": 2926, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "List-Item Student": {"nodeId": "I485:13051;4608:5046;499:101605", "originalName": "List-Item Student", "width": 400, "height": 74, "foundIn": "ila-L/Neue Frderung/Schlersuche 4"}, "_Wizard/Neue Frderung/Schritt 2: Anlsse": {"nodeId": "I485:63624;4608:5046", "originalName": "_Wizard/Neue Förderung/Schritt 2: Anlässe", "width": 432, "height": 574, "foundIn": "ila-L/Neue Frderung/Schlersuche 7"}, "List-Item": {"nodeId": "I485:63624;4608:5046;499:101753", "originalName": "List-Item", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schlersuche 7"}, "Input Radiobutton": {"nodeId": "I485:63624;4608:5046;499:101753;4732:2027", "originalName": "Input Radiobutton", "width": 24, "height": 24, "foundIn": "ila-L/Neue Frderung/Schlersuche 7"}, "Input Radiobutton extended": {"nodeId": "I485:63624;4608:5046;499:101758", "originalName": "Input Radiobutton extended", "width": 432, "height": 110, "foundIn": "ila-L/Neue Frderung/Schlersuche 7"}, "Tag Icon": {"nodeId": "I485:63624;4608:5046;499:101758;8204:10651", "originalName": "Tag Icon", "width": 32, "height": 32, "foundIn": "ila-L/Neue Frderung/Schlersuche 7"}, "_Wizard/Neue Frderung/Schritt 3: Zusammenfassung": {"nodeId": "I485:66083;4608:5046", "originalName": "_Wizard/Neue Förderung/Schritt 3: Zusammenfassung", "width": 432, "height": 652, "foundIn": "ila-L/Neue Frderung/Schlersuche 10"}, "_Wizard/Neue Frderung/Schritt 1: Schlersuche Filter": {"nodeId": "I557:123196;4608:5046", "originalName": "_Wizard/Neue Förderung/Schritt 1: Schülersuche Filter", "width": 432, "height": 2946, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 1"}, "List-Item Student 4": {"nodeId": "I557:123206;4608:5046;499:101458", "originalName": "List-Item Student 4", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 2"}, "List-Item Student 14": {"nodeId": "I557:123206;4608:5046;499:101483", "originalName": "List-Item Student 14", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 2"}, "List-Item Student 15": {"nodeId": "I557:123206;4608:5046;499:101487", "originalName": "List-Item Student 15", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 2"}, "List-Item Student 16": {"nodeId": "I557:123206;4608:5046;499:101488", "originalName": "List-Item Student 16", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 2"}, "List-Item Student 1": {"nodeId": "I557:123216;4608:5046;499:101375", "originalName": "List-Item Student 1", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 2": {"nodeId": "I557:123216;4608:5046;499:101376", "originalName": "List-Item Student 2", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 3": {"nodeId": "I557:123216;4608:5046;499:101377", "originalName": "List-Item Student 3", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 10": {"nodeId": "I557:123216;4608:5046;499:101396", "originalName": "List-Item Student 10", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 11": {"nodeId": "I557:123216;4608:5046;499:101397", "originalName": "List-Item Student 11", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 12": {"nodeId": "I557:123216;4608:5046;499:101398", "originalName": "List-Item Student 12", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 13": {"nodeId": "I557:123216;4608:5046;499:101402", "originalName": "List-Item Student 13", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 17": {"nodeId": "I557:123216;4608:5046;499:101415", "originalName": "List-Item Student 17", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 18": {"nodeId": "I557:123216;4608:5046;499:101416", "originalName": "List-Item Student 18", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 19": {"nodeId": "I557:123216;4608:5046;499:101417", "originalName": "List-Item Student 19", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 20": {"nodeId": "I557:123216;4608:5046;499:101421", "originalName": "List-Item Student 20", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 21": {"nodeId": "I557:123216;4608:5046;499:101422", "originalName": "List-Item Student 21", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "List-Item Student 22": {"nodeId": "I557:123216;4608:5046;499:101426", "originalName": "List-Item Student 22", "width": 448, "height": 74, "foundIn": "ila-L/Neue Frderung/Schritt 1: Schlersuche 3"}, "Modal Stepper": {"nodeId": "1:80607", "originalName": "Modal Stepper", "width": 1024, "height": 900, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "Name": {"nodeId": "I1:80607;7227:20816;7227:18936", "originalName": "Name", "width": 109, "height": 32, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "x": {"nodeId": "I1:80607;7227:20816;7227:18940;4099:640", "originalName": "x", "width": 24, "height": 24, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "_Stepper/Frderziele hinzufgen/Schritt 1: Bereiche Klasse <2": {"nodeId": "I1:80607;5027:2781", "originalName": "_Stepper/Förderziele hinzufügen/Schritt 1: Bereiche Klasse <2", "width": 864, "height": 788, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "Card Category": {"nodeId": "I1:80607;5027:2781;9:74279", "originalName": "Card Category", "width": 192, "height": 192, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "Toggle Inverted": {"nodeId": "I1:80607;5027:2781;9:74286", "originalName": "Toggle Inverted", "width": 56, "height": 32, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "_Action Bar Floating": {"nodeId": "I1:80607;7227:18417", "originalName": "_Action Bar Floating", "width": 720, "height": 64, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "Icon Button Inverted": {"nodeId": "I1:80607;7227:18417;7520:7357", "originalName": "Icon Button Inverted", "width": 48, "height": 48, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "Next": {"nodeId": "I1:80607;7227:18417;7227:18328", "originalName": "Next", "width": 48, "height": 48, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "_Stepper/Frderziele hinzufgen/Schritt 2: Kompetenzen": {"nodeId": "I1:80618;5027:2781", "originalName": "_Stepper/Förderziele hinzufügen/Schritt 2: Kompetenzen", "width": 1120, "height": 720, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Toggle View": {"nodeId": "I1:80618;5027:2781;9:74172", "originalName": "Toggle View", "width": 126, "height": 32, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Card Skill": {"nodeId": "I1:80618;5027:2781;9:74174", "originalName": "Card Skill", "width": 260, "height": 280, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Action Bar": {"nodeId": "I1:80618;7227:18417", "originalName": "Action Bar", "width": 720, "height": 64, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "_Stepper/Frderziele hinzufgen/Schritt 2: Kompetenzen Gruppiert": {"nodeId": "I1:80854;5027:2781", "originalName": "_Stepper/Förderziele hinzufügen/Schritt 2: Kompetenzen Gruppiert", "width": 1120, "height": 720, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Filter Bar": {"nodeId": "I1:80854;5027:2781;9:74164", "originalName": "Filter Bar", "width": 720, "height": 32, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Card Group": {"nodeId": "I1:80854;5027:2781;9:74125", "originalName": "Card Group", "width": 260, "height": 280, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "_Stepper/Frderziele hinzufgen/Schritt 3: Zusammenfassung": {"nodeId": "I1:81392;5027:2781", "originalName": "_Stepper/Förderziele hinzufügen/Schritt 3: Zusammenfassung", "width": 864, "height": 788, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Card Target Compact": {"nodeId": "I1:81392;5027:2781;9:74078", "originalName": "Card Target Compact", "width": 267, "height": 136, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "Link Inverted": {"nodeId": "I1:81392;5027:2781;9:74083", "originalName": "Link Inverted", "width": 134, "height": 24, "foundIn": "IF-L/Frderung-Step 2-Lesen"}, "_Stepper/Frderziele hinzufgen/Schritt 1: Bereiche Klasse >2": {"nodeId": "I1:81434;5027:2781", "originalName": "_Stepper/Förderziele hinzufügen/Schritt 1: Bereiche Klasse >2", "width": 1120, "height": 720, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}, "Placeholder": {"nodeId": "I1:81434;5027:2781;9:74256", "originalName": "Placeholder", "width": 192, "height": 192, "foundIn": "ila-L/Frderziele hinzufgen/Schritt 1 Frderbereich"}};;
  return COMPONENT_INDEX;
}

async function findComponentByName(name) {
  const normalize = (s) => {
    let r = '';
    for (let i = 0; i < s.length; i++) {
      if (s.charCodeAt(i) < 128) r += s[i];
    }
    return r.replace(/\s+/g, ' ').trim();
  };
  
  const norm = normalize(name);
  const index = await loadComponentIndex();
  
  // 1. Exakter Match im Index
  if (index[name]) {
    const entry = index[name];
    const node = await figma.getNodeByIdAsync(entry.nodeId);
    if (node) return node;
  }
  
  // 2. Normalisierter Match im Index
  if (index[norm]) {
    const entry = index[norm];
    const node = await figma.getNodeByIdAsync(entry.nodeId);
    if (node) return node;
  }
  
  // 3. Partial Match im Index
  for (const [key, entry] of Object.entries(index)) {
    if (normalize(key).includes(norm) || norm.includes(normalize(key))) {
      const node = await figma.getNodeByIdAsync(entry.nodeId);
      if (node) return node;
    }
  }
  
  return null;
}

function getOrCreatePage(pageName) {
  const existing = figma.root.children.find((page) => page.name === pageName);
  if (existing) return existing;
  const newPage = figma.createPage();
  newPage.name = pageName;
  return newPage;
}

async function applyLabel(instance, label) {
  const textNodes = [];
  function findText(node) {
    if (node.type === "TEXT") textNodes.push(node);
    if ("children" in node) node.children.forEach(findText);
  }
  findText(instance);
  if (textNodes.length > 0) {
    try {
      await figma.loadFontAsync(textNodes[0].fontName);
      textNodes[0].characters = label;
    } catch(e) {}
  }
}

async function buildScreen(spec) {
  const errors = [];
  let width, height;
  if (spec.width && spec.height) {
    width = spec.width;
    height = spec.height;
  } else {
    const sizeKey = spec.size in FRAME_SIZES ? spec.size : "desktop";
    width = FRAME_SIZES[sizeKey].width;
    height = FRAME_SIZES[sizeKey].height;
  }

  // Alle Fonts zuerst laden — vor allem anderen
  figma.ui.postMessage({ type: "status", message: "Lade Fonts..." });
  const allFonts = [
    ["Noto Sans Display", ["Thin","ExtraLight","Light","Regular","Medium","SemiBold","Bold","ExtraBold","Black"]],
    ["Noto Sans", ["Thin","ExtraLight","Light","Regular","Medium","SemiBold","Bold","ExtraBold","Black"]],
    ["Inter", ["Thin","ExtraLight","Light","Regular","Medium","SemiBold","Bold","ExtraBold","Black"]],
    ["Roboto", ["Thin","Light","Regular","Medium","Bold","Black"]],
  ];
  for (const [family, styles] of allFonts) {
    for (const style of styles) {
      try { await figma.loadFontAsync({ family, style }); } catch(e) {}
    }
  }

  // Zielseite laden
  figma.ui.postMessage({ type: "status", message: "Bereite Seite vor..." });
  const targetPage = figma.root.children.find(p => p.name === spec.page);
  if (targetPage) {
    await targetPage.loadAsync();
    await figma.setCurrentPageAsync(targetPage);
  } else {
    const newPage = figma.createPage();
    newPage.name = spec.page;
    await figma.setCurrentPageAsync(newPage);
  }

  // Frame anlegen
  const frame = figma.createFrame();
  frame.name = spec.screen_name;
  frame.resize(width, height);
  frame.x = 0;
  frame.y = 0;
  frame.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];

  figma.ui.postMessage({ type: "status", message: "Füge Komponenten ein..." });

  for (const compSpec of spec.components) {
    // Node-ID direkt wenn angegeben
    let component = null;
    if (compSpec.nodeId) {
      try {
        const node = await figma.getNodeByIdAsync(compSpec.nodeId);
        if (node) component = node;
      } catch(e) {}
    }
    if (!component) component = await findComponentByName(compSpec.name);

    if (!component) {
      errors.push(`Komponente nicht gefunden: "${compSpec.name}"`);
      continue;
    }

    try {
      // Alle möglichen Fonts laden
      const fontFamilies = [
        "Noto Sans Display", "Noto Sans Display Condensed", 
        "Noto Sans", "Inter", "Roboto", "Arial", "Helvetica",
        "SF Pro Display", "SF Pro Text"
      ];
      const fontStyles = [
        "Thin", "Thin Italic", "ExtraLight", "ExtraLight Italic",
        "Light", "Light Italic", "Regular", "Italic",
        "Medium", "Medium Italic", "SemiBold", "SemiBold Italic",
        "Bold", "Bold Italic", "ExtraBold", "ExtraBold Italic",
        "Black", "Black Italic"
      ];
      for (const family of fontFamilies) {
        for (const style of fontStyles) {
          try { await figma.loadFontAsync({ family, style }); } catch(e) {}
        }
      }

      let instance;
      if (component.type === "COMPONENT") {
        instance = component.createInstance();
      } else {
        instance = component.clone();
      }
      instance.x = compSpec.x;
      instance.y = compSpec.y;
      frame.appendChild(instance);

      if (compSpec.label) {
        await applyLabel(instance, compSpec.label);
      }
    } catch (err) {
      errors.push(`Fehler bei "${compSpec.name}": ${err.message}`);
    }
  }

  figma.viewport.scrollAndZoomIntoView([frame]);

  const success = errors.length === 0;
  const message = success
    ? `Screen "${spec.screen_name}" erstellt (${width}×${height}px).`
    : `Screen "${spec.screen_name}" erstellt — ${errors.length} Fehler.`;

  return { type: "result", success, message, errors };
}

figma.showUI(__html__, { width: 480, height: 560, title: "ILA Screen Builder" });

figma.ui.onmessage = async (msg) => {
  if (msg.type === "cancel") {
    figma.closePlugin();
    return;
  }

  if (msg.type === "build-screen" && msg.json) {
    let spec;
    try {
      spec = JSON.parse(msg.json);
    } catch (parseErr) {
      figma.ui.postMessage({ type: "result", success: false, message: `Ungültiges JSON: ${parseErr.message}`, errors: [] });
      return;
    }

    if (!spec.screen_name || !spec.page || !spec.components) {
      figma.ui.postMessage({ type: "result", success: false, message: "Pflichtfelder fehlen: screen_name, page, components", errors: [] });
      return;
    }

    try {
      const result = await buildScreen(spec);
      figma.ui.postMessage(result);
    } catch (err) {
      figma.ui.postMessage({ type: "result", success: false, message: `Fehler: ${err.message}`, errors: [err.message] });
    }
  }
};
