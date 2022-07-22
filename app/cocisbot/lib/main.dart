import 'dart:convert';
import 'package:bubble/bubble.dart';
import 'package:flutter/material.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:http/http.dart' as http;
// import 'dart:async';
// import 'package:flutter/material.dart';
// import 'package:flutter/services.dart';
// import 'package:rxdart/rxdart.dart';
// import 'package:sound_stream/sound_stream.dart'
// // Copyright 2021 Google LLC
// //
// // Licensed under the Apache License, Version 2.0 (the "License");
// // you may not use this file except in compliance with the License.
// // You may obtain a copy of the License at
// //
// // http://www.apache.org/licenses/LICENSE-2.0
// //
// // Unless required by applicable law or agreed to in writing, software
// // distributed under the License is distributed on an "AS IS" BASIS,
// // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// // See the License for the specific language governing permissions and
// // limitations under the License.


// // TODO import Dialogflow


// class Chat extends StatefulWidget {
//   Chat({Key key}) : super(key: key);

//   @override
//   _ChatState createState() => _ChatState();
// }

// class _ChatState extends State<Chat> {
//   final List<ChatMessage> _messages = <ChatMessage>[];
//   final TextEditingController _textController = TextEditingController();

//   bool _isRecording = false;

//   RecorderStream _recorder = RecorderStream();
//   StreamSubscription _recorderStatus;
//   StreamSubscription<List<int>> _audioStreamSubscription;
//   BehaviorSubject<List<int>> _audioStream;

//   // TODO DialogflowGrpc class instance

//   @override
//   void initState() {
//     super.initState();
//     initPlugin();
//   }

//   @override
//   void dispose() {
//     _recorderStatus?.cancel();
//     _audioStreamSubscription?.cancel();
//     super.dispose();
//   }

//   // Platform messages are asynchronous, so we initialize in an async method.
//   Future<void> initPlugin() async {
//     _recorderStatus = _recorder.status.listen((status) {
//       if (mounted)
//         setState(() {
//           _isRecording = status == SoundStreamStatus.Playing;
//         });
//     });

//     await Future.wait([
//       _recorder.initialize()
//     ]);



//     // TODO Get a Service account

//   }

//   void stopStream() async {
//     await _recorder.stop();
//     await _audioStreamSubscription?.cancel();
//     await _audioStream?.close();
//   }

//   void handleSubmitted(text) async {
//     print(text);
//     _textController.clear();

//     //TODO Dialogflow Code

//   }

//   void handleStream() async {
//     _recorder.start();

//     _audioStream = BehaviorSubject<List<int>>();
//     _audioStreamSubscription = _recorder.audioStream.listen((data) {
//       print(data);
//       _audioStream.add(data);
//     });


//     // TODO Create SpeechContexts
//     // Create an audio InputConfig

//     // TODO Make the streamingDetectIntent call, with the InputConfig and the audioStream
//     // TODO Get the transcript and detectedIntent and show on screen

//   }

//   // The chat interface
//   //
//   //------------------------------------------------------------------------------------
//   @override
//   Widget build(BuildContext context) {
//     return Column(children: <Widget>[
//       Flexible(
//           child: ListView.builder(
//             padding: EdgeInsets.all(8.0),
//             reverse: true,
//             itemBuilder: (_, int index) => _messages[index],
//             itemCount: _messages.length,
//           )),
//       Divider(height: 1.0),
//       Container(
//           decoration: BoxDecoration(color: Theme.of(context).cardColor),
//           child: IconTheme(
//             data: IconThemeData(color: Theme.of(context).accentColor),
//             child: Container(
//               margin: const EdgeInsets.symmetric(horizontal: 8.0),
//               child: Row(
//                 children: <Widget>[
//                   Flexible(
//                     child: TextField(
//                       controller: _textController,
//                       onSubmitted: handleSubmitted,
//                       decoration: InputDecoration.collapsed(hintText: "Send a message"),
//                     ),
//                   ),
//                   Container(
//                     margin: EdgeInsets.symmetric(horizontal: 4.0),
//                     child: IconButton(
//                       icon: Icon(Icons.send),
//                       onPressed: () => handleSubmitted(_textController.text),
//                     ),
//                   ),
//                   IconButton(
//                     iconSize: 30.0,
//                     icon: Icon(_isRecording ? Icons.mic_off : Icons.mic),
//                     onPressed: _isRecording ? stopStream : handleStream,
//                   ),
//                 ],
//               ),
//             ),
//           )
//       ),
//     ]);
//   }
// }

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


  List<String> _data = [];
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
           SizedBox(
                height: 100,
              ),
          MessageBar(
            onSend: (msg) => this._getResponse(msg),
            actions: [
              InkWell(
                child: Icon(
                  Icons.add,
                  color: Colors.black,
                  size: 24,
                ),
                onTap: () {},
              ),
              Padding(
                padding: EdgeInsets.only(left: 8, right: 8),
                child: InkWell(
                  child: Icon(
                    Icons.camera_alt,
                    color: Colors.green,
                    size: 24,
                  ),
                  onTap: () {},
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
    if (msg.length>0){
      this._insertSingleItem(msg);
      var client = _getClient();
      try{
        client.get(BOT_URL+"?query="+msg)
        ..then((response){
          Map<String, dynamic> data = jsonDecode(response.body);
          _insertSingleItem(data['response']+"<bot>");
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