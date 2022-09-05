import 'dart:convert';
import 'package:bubble/bubble.dart';
import 'package:flutter/material.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:http/http.dart' as http;
import 'package:text_to_speech/text_to_speech.dart';


void main() => runApp(MyApp());
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Chatbot Flask',
      theme: ThemeData(
primarySwatch: Colors.green,
      ),
      home: MyHomePage(title: 'COCIS BOT'),
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


  List<String> _data = ['HI THIS IS THE COCIS BOT \n ASK ME QUESTIONS LIKE WHERE IS THE BOARD ROOM FIND JOHN DOE<bot>'];
  static const String BOT_URL = "https://cocisbot.herokuapp.com/getmsg/"; // replace with server address
  TextEditingController _queryController = TextEditingController();
@override
  Widget build(BuildContext context) {
return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text("COCIS BOT"),
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
           
          MessageBar(
            onSend: (msg) => this._getResponse(msg),
            actions: [
              InkWell(
                child: Icon(
                  Icons.mic,
                  color: Colors.black,
                  size: 24,
                ),
                onTap: () {},
              )
              
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