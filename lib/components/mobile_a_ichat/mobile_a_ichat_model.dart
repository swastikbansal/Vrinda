import '/backend/api_requests/api_calls.dart';
import '/components/ai_bottom_sheet/ai_bottom_sheet_widget.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_toggle_icon.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'dart:ui';
import 'mobile_a_ichat_widget.dart' show MobileAIchatWidget;
import 'package:aligned_tooltip/aligned_tooltip.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:lottie/lottie.dart';
import 'package:provider/provider.dart';

class MobileAIchatModel extends FlutterFlowModel<MobileAIchatWidget> {
  ///  State fields for stateful widgets in this component.

  // State field(s) for ListView widget.
  ScrollController? listViewController;
  // State field(s) for TextField widget.
  FocusNode? textFieldFocusNode;
  TextEditingController? textController;
  String? Function(BuildContext, String?)? textControllerValidator;
  // Stores action output result for [Backend Call - API (Ultron)] action in Icon widget.
  ApiCallResponse? _apiResultyc4;
  set apiResultyc4(ApiCallResponse? value) {
    _apiResultyc4 = value;
    debugLogWidgetClass(this);
  }

  ApiCallResponse? get apiResultyc4 => _apiResultyc4;

  final Map<String, DebugDataField> debugGeneratorVariables = {};
  final Map<String, DebugDataField> debugBackendQueries = {};
  final Map<String, FlutterFlowModel> widgetBuilderComponents = {};
  @override
  void initState(BuildContext context) {
    listViewController = ScrollController();
  }

  @override
  void dispose() {
    listViewController?.dispose();
    textFieldFocusNode?.dispose();
    textController?.dispose();
  }

  @override
  WidgetClassDebugData toWidgetClassDebugData() => WidgetClassDebugData(
        widgetStates: {
          'textFieldText': debugSerializeParam(
            textController?.text,
            ParamType.String,
            link:
                'https://app.flutterflow.io/project/vrinda-kriyeta4-tllf8o?tab=uiBuilder&page=mobileAIchat',
            name: 'String',
            nullable: true,
          )
        },
        actionOutputs: {
          'apiResultyc4': debugSerializeParam(
            apiResultyc4,
            ParamType.ApiResponse,
            link:
                'https://app.flutterflow.io/project/vrinda-kriyeta4-tllf8o?tab=uiBuilder&page=mobileAIchat',
            name: 'ApiCallResponse',
            nullable: true,
          )
        },
        generatorVariables: debugGeneratorVariables,
        backendQueries: debugBackendQueries,
        componentStates: {
          ...widgetBuilderComponents.map(
            (key, value) => MapEntry(
              key,
              value.toWidgetClassDebugData(),
            ),
          ),
        }.withoutNulls,
        link:
            'https://app.flutterflow.io/project/vrinda-kriyeta4-tllf8o/tab=uiBuilder&page=mobileAIchat',
        searchReference: 'reference=Ogxtb2JpbGVBSWNoYXRQAFoMbW9iaWxlQUljaGF0',
        widgetClassName: 'mobileAIchat',
      );
}
