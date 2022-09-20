import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:http/http.dart' as http;
import 'package:speech_to_text/speech_recognition_result.dart';
import 'package:text_to_speech/text_to_speech.dart';
import 'package:speech_to_text/speech_to_text.dart';
import 'package:quick_feedback/quick_feedback.dart';
import 'package:internet_checker_banner/internet_checker_banner.dart';
import 'package:flutter_onboarding_screen/OnbordingData.dart';
import 'package:flutter_onboarding_screen/flutteronboardingscreens.dart';







void main() => runApp(MyApp());
class MyApp extends StatelessWidget {
  
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Chatbot Flask',
      theme: ThemeData(
primarySwatch: Colors.green,
      ),
      home: TestScreen(),
    );
  }
}
class TestScreen extends StatelessWidget {
    /*here we have a list of OnbordingScreen which we want to have, each OnbordingScreen have a imagePath,title and an desc.
      */
  final List<OnbordingData> list = [
    OnbordingData(
      imagePath: "assets/logo.png",
      title: "COCIS BOT",
      desc:"This app helps new college visitors as well students and lectures get around the college",
    ),
    OnbordingData(
      imagePath: "assets/logo.png",
      title: "Fnding Offices",
      desc:"You can use this app to get the location of offices forexample where is the boardroom",
    ),
    OnbordingData(
      imagePath: "assets/logo.png",
      title: "Finding personnel",
      desc:"Find out where college personnel sit forexample where is the principal",
    ),
  ];

  @override
  Widget build(BuildContext context) {
    /* remove the back button in the AppBar is to set automaticallyImplyLeading to false
  here we need to pass the list and the route for the next page to be opened after this. */
    return new IntroScreen(list,MaterialPageRoute(builder: (context) => MyHomePage(title: "COCIS BOT")),
    );
  }
}
class MyHomePage extends StatefulWidget {
MyHomePage({Key? key, required this.title}) : super(key: key);
final String title;
@override
  _MyHomePageState createState() => _MyHomePageState();
}
class _MyHomePageState extends State<MyHomePage> {
 GlobalKey<AnimatedListState> _listKey =  GlobalKey();


  List<String> _data = [];
  static const String BOT_URL = "https://cocischatbott.herokuapp.com/api/getmsg/"; // replace with server address
  TextEditingController _queryController = TextEditingController();
  
  late  TextEditingController _textController = TextEditingController();


  SpeechToText _speechToText = SpeechToText();
  bool _speechEnabled = false;
  String _lastWords = '';

  @override
  void initState() {
    super.initState();
     // TODO: implement initState
    InternetCheckerBanner().initialize(context, title: "No internet access");
    super.initState();
    _initSpeech();
  }
    @override
  void dispose() {
    // TODO: implement dispose
    InternetCheckerBanner().dispose();
    super.dispose();
  }


  /// This has to happen only once per app
  void _initSpeech() async {
    _speechEnabled = await _speechToText.initialize();
    setState(() {});
  }

  /// Each time to start a speech recognition session
  void _startListening() async {
    await _speechToText.listen(onResult: _onSpeechResult);
    setState(() {});
  }

  /// Manually stop the active speech recognition session
  /// Note that there are also timeouts that each platform enforces
  /// and the SpeechToText plugin supports setting timeouts on the
  /// listen method.
  void _stopListening() async {
    await _speechToText.stop();
    setState(() {});
  }

  /// This is the callback that the SpeechToText plugin calls when
  /// the platform returns recognized words.
  void _onSpeechResult(SpeechRecognitionResult result) {
    setState(() {
      _lastWords = result.recognizedWords;
      _textController.text=_lastWords;
    });
  } 


  void _showFeedback(context) {
    showDialog(
      context: context,
      builder: (context) {
        return QuickFeedback(
          title: 'Leave a feedback', // Title of dialog
          showTextBox: true, // default false
          textBoxHint:
              'Share your feedback', // Feedback text field hint text default: Tell us more
          submitText: 'SUBMIT', // submit button text default: SUBMIT
          onSubmitCallback: (feedback) {
                 final snackBar = SnackBar(
            content: const Text('Thanks! for the feedback'),
            action: SnackBarAction(
              label: 'OK',
              onPressed: () {
                // Some code to undo the change.
              },
            ),
          );
          _feedback(feedback['rating'].toString(), feedback['feedback']);
            print('$feedback');
            print(feedback['rating']);
            feedback.keys.forEach((k) => print(k));
            feedback.values.forEach((v) => print(v));
            
             // map { rating: 2, feedback: 'some feedback' }
            // _feedback(feedback.rating, feedback.feedback);
               ScaffoldMessenger.of(context).showSnackBar(snackBar);
               Navigator.of(context).pop();
            // Navigator.of(context).pop();
          },
          askLaterText: 'ASK LATER',
          onAskLaterCallback: () {
            print('Do something on ask later click');
          },
        );
      },
    );
  }
  
 

@override
  Widget build(BuildContext context) {
return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text("COCIS BOT"),
          actions: <Widget>[
    IconButton(
      icon: Icon(
        Icons.feedback,
        color: Colors.white,
      ),
      onPressed: () => _showFeedback(context),
    )
  ],
      ),
      body: Stack(
        
        children: [
       
            AnimatedList(
            // key to call remove and insert from anywhere
            key: _listKey,
            initialItemCount: _data.length,
            itemBuilder: (BuildContext context, int index, Animation<double> animation){
              return _buildItem(_data[index], animation, index);
            }
          ),
           SizedBox(
             height: 2000000,

           ),
          // MessageBar(
          //   onSend: (msg) => this._getResponse(msg),
          //   actions: [
          //     InkWell(
          //       child: Icon(
          //         Icons.mic,
          //         color: Colors.black,
          //         size: 24,
          //       ),
          //       onTap: () {},
          //     )
              
          //   ],
          // ),
           Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
           
            Container(
              // color: Color(0xffF4F4F5),
              padding: const EdgeInsets.symmetric(
                vertical: 8,
                horizontal: 16,
              ),
              child: Row(
                children: <Widget>[
                  // ...actions,
                        InkWell(
                child: Icon(
                  _speechToText.isNotListening ? Icons.mic_off : Icons.mic,
                  color: _speechToText.isNotListening ? Colors.green : Colors.red,
                  size: 24,
                ),
                onTap: _speechToText.isNotListening ? _startListening : _stopListening,
              ),
                  Expanded(
                    child: Container(
                      child: TextField(
                        controller: _textController,
                        keyboardType: TextInputType.multiline,
                        textCapitalization: TextCapitalization.sentences,
                        minLines: 1,
                        maxLines: 3,
                        // onChanged: onTextChanged,
                        decoration: InputDecoration(
                          hintText: "Type your question here",
                          hintMaxLines: 1,
                          contentPadding: const EdgeInsets.symmetric(
                              horizontal: 8.0, vertical: 10),
                          hintStyle: TextStyle(
                            fontSize: 16,
                          ),
                          fillColor: Colors.white,
                          filled: true,
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(30.0),
                            borderSide: const BorderSide(
                              color: Colors.white,
                              width: 0.2,
                            ),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(30.0),
                            borderSide: const BorderSide(
                              color: Colors.black26,
                              width: 0.2,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(left: 16),
                    child: InkWell(
                      child: Icon(
                        Icons.send,
                        color: Colors.blue,
                        size: 24,
                      ),
                      onTap: () {
                      
                      
                           this._getResponse(_textController.text);
                          
                          _textController.text = '';
                        
                      },
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        ],
      ),
      
    );
  }
http.Client _getClient(){
    return http.Client();
  }
void _getResponse(String msg){
  TextToSpeech tts = TextToSpeech();
    if (msg.length>0){
      this._insertSingleItem(msg);
      var client = _getClient();
      try{
        client.get(BOT_URL+"?query="+msg)
        ..then((response){
          Map<String, dynamic> data = jsonDecode(response.body);
          _insertSingleItem(data['response']+"<bot>");
          tts.speak(data['response']);
});
      }catch(e){
        print("Failed -> $e");
      }finally{
        client.close();
        _queryController.clear();
      }
    }
  }

  void _feedback(String title, String info){
  
 Map data = {
    'title': "Rating: "+title,
     'body': info

  };

    var body = json.encode(data);
   
      var client = _getClient();
      try{
        client.post
        ("https://api.github.com/repos/theebruno/cocischatbot/issues",
        
         headers: {"Content-Type": "application/json","Authorization": "Bearer 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"},
          body: body
          )
        ..then((response){
          // Map<String, dynamic> data = jsonDecode(response.body);
          // _insertSingleItem(data['response']+"<bot>");
         
});
      }catch(e){
        print("Failed -> $e");
      }finally{
        client.close();
        
      }
    
  }
  
  
void _insertSingleItem(String message){
_data.add(message); 

_listKey.currentState!.insertItem(_data.length-1);


  }
Widget _buildItem(String item, Animation<double> animation,int index){
    bool mine = item.endsWith("<bot>");
    return SizeTransition(
      sizeFactor: animation,
      child: Padding(padding: EdgeInsets.only(top: 10),
      child: Container(
        alignment: mine ?  Alignment.topLeft : Alignment.topRight,
child : BubbleSpecialThree(
        text: item.replaceAll("<bot>", ""),
        color: mine ? Color(0xFFE8E8EE) : Color.fromRGBO(225, 255, 199, 1.0),
         tail: true,
        isSender: mine ? false : true,
        
)),
    )
);
  }
}