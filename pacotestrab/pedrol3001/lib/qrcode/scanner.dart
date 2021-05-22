import 'dart:io';
import 'package:flutter/material.dart';
import 'package:qr_code_scanner/qr_code_scanner.dart';

class QrCodeScanner extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _QrCodeScannerState();
}

class _QrCodeScannerState extends State<QrCodeScanner> {
  QRViewController? controller;
  final GlobalKey qrKey = GlobalKey(debugLabel: 'QrCodeScanner');

  @override
  void reassemble() {
    super.reassemble();
    if (Platform.isAndroid) {
      controller!.pauseCamera();
    }
    controller!.resumeCamera();
  }

  @override
  Widget build(BuildContext context) {
    var iconColor = Colors.grey[400];
    return Scaffold(
      body: Stack(
        children: <Widget>[
          Expanded(flex: 4, child: _buildQrView(context)),
          Align(
            alignment: Alignment.bottomCenter,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Container(
                  margin: EdgeInsets.all(8),
                  child: IconButton(
                    onPressed: () async {
                      setState(() {
                        Navigator.pop(context, "");
                      });
                      controller?.stopCamera();
                    },
                    iconSize: 40,
                    color: Colors.white,
                    icon: Icon(Icons.close, color: iconColor),
                  ),
                ),
                Container(
                  margin: EdgeInsets.all(8),
                  child: IconButton(
                      onPressed: () async {
                        await controller?.toggleFlash();
                        setState(() {});
                      },
                      iconSize: 40,
                      color: Colors.white,
                      icon: FutureBuilder(
                        future: controller?.getFlashStatus(),
                        builder: (context, snapshot) {
                          if (snapshot.data != true) {
                            return Icon(Icons.flash_off, color: iconColor);
                          } else {
                            return Icon(Icons.flash_on, color: iconColor);
                          }
                        },
                      )),
                ),
                Container(
                  margin: EdgeInsets.all(8),
                  child: IconButton(
                      onPressed: () async {
                        await controller?.flipCamera();
                        setState(() {});
                      },
                      iconSize: 40,
                      icon: FutureBuilder(
                        future: controller?.getCameraInfo(),
                        builder: (context, snapshot) {
                          if (snapshot.data != CameraFacing.back) {
                            return Icon(Icons.camera_front, color: iconColor);
                          } else {
                            return Icon(Icons.camera, color: iconColor);
                          }
                        },
                      )),
                )
              ],
            ),
          )
        ],
      ),
    );
  }

  Widget _buildQrView(BuildContext context) {
    // For this example we check how width or tall the device is and change the scanArea and overlay accordingly.
    var scanArea = (MediaQuery.of(context).size.width < 400 ||
            MediaQuery.of(context).size.height < 400)
        ? 250.0
        : 500.0;
    // To ensure the Scanner view is properly sizes after rotation
    // we need to listen for Flutter SizeChanged notification and update controller
    return QRView(
      key: qrKey,
      onQRViewCreated: _onQRViewCreated,
      overlay: QrScannerOverlayShape(
          borderColor: Colors.red,
          borderRadius: 8,
          borderLength: 20,
          borderWidth: 8,
          cutOutSize: scanArea),
    );
  }

  void _onQRViewCreated(QRViewController controller) {
    setState(() {
      this.controller = controller;
    });
    controller.scannedDataStream.listen((scanData) {
      if (scanData.format == BarcodeFormat.qrcode) {
        Navigator.pop(context, '{"error": 0, "value": "${scanData.code}"}');
        controller.dispose();
      } else {
        Navigator.pop(context, '{"error": -1, "value": "Not a QrCode"}');
        controller.dispose();
      }
    })
      ..onError((e) {
        Navigator.pop(context,
            '{"error": -1, "value": "Error readding QrCode, try again"}');
        controller.dispose();
      });
  }

  @override
  void dispose() {
    controller?.dispose();
    super.dispose();
  }
}
