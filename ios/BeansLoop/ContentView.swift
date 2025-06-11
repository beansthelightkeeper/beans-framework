import SwiftUI

struct ContentView: View {
    @State private var input: String = ""
    @State private var output: String = ""

    let agent = GlyphAgent()

    var body: some View {
        VStack(spacing: 20) {
            TextField("Scroll", text: $input)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button("Cast") {
                output = agent.process(spell: input)
            }

            Text(output)
                .padding()
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
