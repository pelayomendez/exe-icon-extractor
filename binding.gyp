{
  "targets": [
    {
      "target_name": "module",
      "product_extension": "node",
      "include_dirs" : [ "src" ],
      "conditions": [
        ['OS=="win"', {
          'cflags': [
            '/EHa',
          ],
          "sources": ["src/module.cc"],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ExceptionHandling': '1',    
              'AdditionalOptions': ['/EHsc']
            }
          }
        },],
      ]
    }
  ]
}