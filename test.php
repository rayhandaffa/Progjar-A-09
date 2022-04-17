<?php
/**
* Store a newly created resource in storage.
*
* @param  \Illuminate\Http\Request  $request
* @return \Illuminate\Http\Response
*/
public function store(Request $request)
{
    $this->validate($request, [
        'nama' => 'required',
        'file' => 'required | file | image| mimes:jpeg,bmp,png,jpg',
        'jenis' => 'required',
        // 'isdingin' => 'required',
        'harga' => 'required',
    ]);
    
    $file = $request->file('file');
    $filename = time()."_".$file->getClientOriginalName();

    $upload_path = 'product_img';
    $file->move($upload_path, $filename);


    $product = new Produk;
    $product->nama = $request->input('nama');
    $product->img_path = $filename;
    $product->jenis = $request->input('jenis');
    // $product->isdingin = $request->input('isdingin');
    $product->harga = $request->input('harga');
    $product->isavail = 1;
    $product->save();
    // return view('admin/manage');
    // return $product->;
    return redirect('/admin/manage')
        ->with('success', 'Produk berhasil di-submit');
}


public function edit(Produk $produk)
{
    return view('admin.edit')
        ->with('produk', $produk);
}

public function update(Request $request, Produk $produk)
{
    $this->validate($request, [
        'nama' => 'required',
        'file' => 'file | image | mimes:jpeg,bmp,png,jpg',
        'jenis' => 'required',
        // 'isdingin' => 'required',
        'harga' => 'required',
    ]);
    
    if ($request->file('file') != null) {
        $file = $request->file('file');
        $filename = time()."_".$file->getClientOriginalName();

        $upload_path = 'product_img';
        $file->move($upload_path, $filename);
    } else {
        $filename = $produk->img_path;
    }
    


    // $product = new Produk;
    $produk->nama = $request->input('nama');
    $produk->img_path = $filename;
    $produk->jenis = $request->input('jenis');
    // $produk->isdingin = $request->input('isdingin');
    $produk->harga = $request->input('harga');
    $produk->isavail = 1;
    $produk->save();

    // return $filename;
    return redirect('/admin/manage')
        ->with('success', 'Produk berhasil di-edit');
}

/**
 * Remove the specified resource from storage.
 *
 * @param  \App\Models\Produk  $produk
 * @return \Illuminate\Http\Response
 */
public function destroy(Produk $produk)
{
    $produk->isavail = 2;
    $produk->save();
    $produk->delete();
    $filename = $produk->img_path;
    // $upload_path = 'product_img';
    File::delete(public_path('product_img/'.$filename));

    return redirect('/admin/manage')
        ->with('success', 'Produk berhasil di-hapus');
}

public function toggleAction(Produk $produk)
{
    // $produkni = Produk::where('id_produk', '=', $produk->id)->first()->get();
    $availnow = $produk->isavail;
    if ($availnow == 0) {
        $produk->isavail = 1;
        $produk->save();
    } else {
        $produk->isavail = 0;
        $produk->save();
    }
    
    return redirect('/admin/manage')
        ->with('success', 'Produk berhasil di-update');
    // $product->isavail = $request->input('toggle');
}