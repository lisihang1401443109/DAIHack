# Duke AI Hackathon 2024


## Three APIS:

1. Agent API
   1. provides agent services
   2. takes `chat_history`, `memory`

2. Segment Anything API
   1. # agent tools
   2. # format
   ```json
   {input:
    {
        file_path: str
        segment_targets: str
    },
    output:
    {
        mask: .py file path,
        error: error message
    } 
   }
   
   ```

3. append furnitures API
   1. # agent tools
   2. # format
   ```json
   {
    input：{
        position: (x, y),
        furniture_image: file_path
    },

    output:{
        new_image: file_path
    }

   } 
   
   
   ```